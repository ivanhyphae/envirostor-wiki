#!/usr/bin/env bash
#
# Wipes all compiled sage-wiki content and state so `sage-wiki compile` can
# rebuild the wiki from scratch. Does NOT touch source material.
#
# Deletes:
#   .manifest.json        - source -> compiled article manifest
#   .sage/                - compile state, wiki.db (NOT git-tracked --
#                            deleting this is NOT recoverable via git)
#   wiki/CHANGELOG.md      - generated changelog
#   wiki/index.md          - generated index
#   wiki/concepts/         - generated concept articles
#   wiki/summaries/        - generated per-source summaries
#   wiki/outputs/          - generated query/write outputs
#   wiki/under_review/     - generated pending-review articles
#   wiki/images/           - generated dataviz charts
#
# Deliberately left alone (these are sources/inputs, not compiled content):
#   raw/                   - original PDFs
#   wiki/pdf2md/           - sage-wiki's configured source dir (see config.yaml)
#   wiki/pdf2md-no-tables/ - separate marker ablation output
#   archive/               - anything already archived
#   wiki/.obsidian/        - Obsidian vault config
#
# Everything deleted here except .sage/ is currently git-tracked and clean,
# so it can be restored with `git checkout -- <path>` if this is run by
# mistake. .sage/wiki.db is gitignored and NOT recoverable that way.
#
# Usage:
#   ./scripts/nuke-wiki.sh          # dry run -- lists what would be deleted
#   ./scripts/nuke-wiki.sh --yes    # actually delete

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

CONFIRM=false
for arg in "$@"; do
  case "$arg" in
    --yes) CONFIRM=true ;;
    *) echo "Unknown option: $arg"; exit 1 ;;
  esac
done

TARGETS=(
  ".manifest.json"
  ".sage"
  "wiki/CHANGELOG.md"
  "wiki/index.md"
  "wiki/concepts"
  "wiki/summaries"
  "wiki/outputs"
  "wiki/under_review"
  "wiki/images"
)

echo "The following will be deleted:"
for t in "${TARGETS[@]}"; do
  if [ -e "$t" ]; then
    size=$(du -sh "$t" 2>/dev/null | cut -f1)
    echo "  $t ($size)"
  else
    echo "  $t (already absent)"
  fi
done
echo ""
echo "Preserved (sources, not compiled content):"
echo "  raw/  wiki/pdf2md/  wiki/pdf2md-no-tables/  archive/  wiki/.obsidian/"
echo ""

if [ "$CONFIRM" = false ]; then
  echo "Dry run only -- nothing deleted. Re-run with --yes to actually delete."
  exit 0
fi

for t in "${TARGETS[@]}"; do
  rm -rf "$t"
done

echo "Done. sage-wiki content wiped."
echo ""
if [ ! -d "wiki/pdf2md" ]; then
  echo "NOTE: config.yaml's configured source path (wiki/pdf2md) does not"
  echo "currently exist on disk -- 'sage-wiki compile' will find 0 sources"
  echo "until that's restored or config.yaml is repointed."
fi
