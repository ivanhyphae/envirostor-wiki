#!/usr/bin/env bash
#
# Batch-process PDFs from raw/ through marker, outputting to wiki/pdf2md/.
# Skips PDFs that already have non-empty output directories.
#
# Usage:
#   ./process-pdfs.sh              # process all unprocessed PDFs
#   ./process-pdfs.sh --force-ocr  # reprocess with --force_ocr (for scanned/image-only PDFs)
#   ./process-pdfs.sh --reprocess  # wipe and reprocess everything
#
# Requires:
#   - GOOGLE_API_KEY in environment (already in ~/.bashrc)
#   - marker venv at /home/ivanh/.venvs/surya/

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
for arg in "$@"; do
  case "$arg" in
    --force-ocr) FORCE_OCR="--force_ocr" ;;
    --reprocess) REPROCESS=true ;;
    --stop-llama) STOP_LLAMA=true ;;
    *) echo "Unknown option: $arg"; exit 1 ;;
  esac
done

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

if [ "$REPROCESS" = true ]; then
  echo "Wiping existing output in $OUT_DIR..."
  rm -rf "$OUT_DIR"/*
fi

# Find unprocessed PDFs (no non-empty output dir yet)
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

count=0
for f in "$RAW_DIR"/*.pdf; do
  [ -f "$f" ] || continue
  name=$(basename "$f" .pdf)
  out_subdir="$OUT_DIR/$name"

  # Skip if output dir exists and has content
  if [ -d "$out_subdir" ] && [ -n "$(ls -A "$out_subdir" 2>/dev/null)" ]; then
    continue
  fi

  cp "$f" "$TMP_DIR/"
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "Nothing to process — all PDFs already have output."
  exit 0
fi

echo "Processing $count PDF(s) with $WORKERS workers..."
[ -n "$FORCE_OCR" ] && echo "  (--force_ocr enabled)"

# marker batch command
"$MARKER_BIN" "$TMP_DIR" \
  --output_dir "$OUT_DIR" \
  --use_llm \
  --llm_service "marker.services.openai.OpenAIService" \
  --config_json "$MARKER_CONFIG" \
  --workers "$WORKERS" \
  $FORCE_OCR

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
