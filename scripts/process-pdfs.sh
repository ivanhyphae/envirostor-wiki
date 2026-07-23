#!/usr/bin/env bash
#
# Batch-process PDFs from raw/ through marker, outputting to wiki/pdf2md/.
# Skips PDFs that already have non-empty output directories.
#
# Usage:
#   ./process-pdfs.sh              # process all unprocessed PDFs
#   ./process-pdfs.sh --force-ocr  # reprocess with --force_ocr (for scanned/image-only PDFs)
#   ./process-pdfs.sh --reprocess  # reprocess everything (overwrites existing output)
#   ./process-pdfs.sh --no-tables  # ablation run: skip table recognition/LLM table
#                                   # correction and render tables as a bare "[Table]"
#                                   # placeholder. Also replaces extracted images with
#                                   # LLM-generated text descriptions (--disable_image_extraction),
#                                   # since sage-wiki only reads markdown text. Always
#                                   # reprocesses everything, into wiki/sources/ (sage-wiki's
#                                   # configured source dir -- see config.yaml), so the
#                                   # original wiki/pdf2md/ corpus is untouched.
#
# Requires:
#   - GOOGLE_API_KEY in environment (already in ~/.bashrc)
#   - marker venv at /home/ivanh/.venvs/surya/
#
# Every run's full output (including marker's own API retry/error logging) is
# tee'd to logs/process-pdfs-<timestamp>.log, with logs/process-pdfs-latest.log
# symlinked to it -- so a run's history survives even if the terminal/VSCode
# is killed mid-run. To make the *process* itself survive that too (not just
# the log), launch it detached, e.g.:
#   setsid nohup ./process-pdfs.sh --no-tables >/dev/null 2>&1 < /dev/null &
# then `tail -f logs/process-pdfs-latest.log` from a fresh terminal to watch it.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

MARKER_BIN="/home/ivanh/.venvs/surya/bin/marker"
MARKER_CONFIG="$REPO_DIR/marker-config.json"
RAW_DIR="$REPO_DIR/raw"
OUT_DIR="$REPO_DIR/wiki/pdf2md"
WORKERS=1

# Parse args
FORCE_OCR=""
REPROCESS=false
STOP_LLAMA=false
NO_TABLES=false
for arg in "$@"; do
  case "$arg" in
    --force-ocr) FORCE_OCR="--force_ocr" ;;
    --reprocess) REPROCESS=true ;;
    --stop-llama) STOP_LLAMA=true ;;
    --no-tables) NO_TABLES=true ;;
    *) echo "Unknown option: $arg"; exit 1 ;;
  esac
done

DISABLE_IMAGE_EXTRACTION=""
if [ "$NO_TABLES" = true ]; then
  MARKER_CONFIG="$REPO_DIR/marker-config-no-tables.json"
  OUT_DIR="$REPO_DIR/wiki/sources"
  REPROCESS=true
  # Replace images with LLM-generated text descriptions instead of extracting
  # them as files -- sage-wiki only reads markdown text, so raw image files
  # are otherwise invisible to it.
  DISABLE_IMAGE_EXTRACTION="--disable_image_extraction"
fi

# Log everything (this script's own output plus marker's stdout/stderr,
# including API retry/error messages) to a timestamped file, in addition to
# the terminal, so the log survives even if the terminal is killed.
LOG_DIR="$REPO_DIR/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/process-pdfs-$(date +%Y%m%d-%H%M%S).log"
ln -sf "$(basename "$LOG_FILE")" "$LOG_DIR/process-pdfs-latest.log"
exec > >(tee -a "$LOG_FILE") 2>&1
echo "Logging to $LOG_FILE"

# Reduce GPU memory fragmentation (recommended by PyTorch for marker's surya models)
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Stop llama-server to free GPU memory for marker's surya models
if [ "$STOP_LLAMA" = true ]; then
  if systemctl --user is-active --quiet llama-server.service; then
    echo "Stopping llama-server to free VRAM..."
    systemctl --user stop llama-server.service
  fi
elif systemctl --user is-active --quiet llama-server.service; then
  echo "Warning: llama-server is running and consuming ~6GB VRAM."
  echo "  If marker runs out of GPU memory, stop it first:"
  echo "    systemctl --user stop llama-server.service"
  echo "  Or re-run with --stop-llama flag."
  echo ""
fi

# Checks
if [ ! -x "$MARKER_BIN" ]; then
  echo "ERROR: marker not found at $MARKER_BIN"
  exit 1
fi
if [ ! -f "$MARKER_CONFIG" ]; then
  echo "ERROR: config not found at $MARKER_CONFIG"
  exit 1
fi
if [ -z "${GOOGLE_API_KEY:-}" ]; then
  echo "ERROR: GOOGLE_API_KEY not set in environment"
  exit 1
fi

mkdir -p "$OUT_DIR"

TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

count=0
for f in "$RAW_DIR"/*.pdf; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .pdf)
  out_subdir="$OUT_DIR/$name"

  # Skip if output dir exists and has content (normal mode only)
  if [ "$REPROCESS" = false ] && [ -d "$out_subdir" ] && [ -n "$(ls -A "$out_subdir" 2>/dev/null)" ]; then
    continue
  fi

  # Only copy to temp dir in normal mode -- reprocess reads from raw/ directly
  if [ "$REPROCESS" = false ]; then
    cp "$f" "$TMP_DIR/"
  fi
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "Nothing to process — all PDFs already have output."
  exit 0
fi

if [ "$REPROCESS" = true ]; then
  echo "Reprocessing $count PDF(s) with $WORKERS workers (overwriting existing output)..."
  TARGET_DIR="$RAW_DIR"
else
  echo "Processing $count PDF(s) with $WORKERS workers..."
  TARGET_DIR="$TMP_DIR"
fi

[ -n "$FORCE_OCR" ] && echo "  (--force_ocr enabled)"

# marker batch command
"$MARKER_BIN" "$TARGET_DIR" \
    --output_dir "$OUT_DIR" \
    --use_llm \
    --llm_service "marker.services.openai.OpenAIService" \
    --config_json "$MARKER_CONFIG" \
    --workers "$WORKERS" \
    $FORCE_OCR \
    $DISABLE_IMAGE_EXTRACTION

echo ""
echo "Done. Checking results..."

# Report
empty=0
ok=0
for f in "$RAW_DIR"/*.pdf; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .pdf)
  out_subdir="$OUT_DIR/$name"
  if [ ! -d "$out_subdir" ] || [ -z "$(ls -A "$out_subdir" 2>/dev/null)" ]; then
    echo "  EMPTY: $name"
    empty=$((empty + 1))
  else
    ok=$((ok + 1))
  fi
done

echo ""
echo "Results: $ok with content, $empty empty/failed"
