#!/usr/bin/env bash
#
# wiki/sources/ is marker's PDF-to-markdown output: one folder per document,
# each containing <name>.md and <name>_meta.json. That layout is fine for
# marker/sage-wiki, but bad for Quartz -- it makes the Explorer sidebar show
# 100+ folders each holding a single identically-named file, and pages end up
# double-nested at /sources/<name>/<name>/.
#
# This flattens things for the Quartz build only, by symlinking each source's
# .md file into site/content/sources/<name>.md (no wrapping folder). It never
# touches wiki/sources/ itself, and re-running it just adds symlinks for any
# new sources and removes stale ones for sources that were deleted.
#
# Usage:
#   ./scripts/sync-quartz-sources.sh
#
# Run this before `npx quartz build` whenever wiki/sources/ has changed
# (i.e. after `sage-wiki compile` or `./process-pdfs.sh`).

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCES_DIR="$REPO_DIR/wiki/sources"
DEST_DIR="$REPO_DIR/site/content/sources"

mkdir -p "$DEST_DIR"

# Remove stale symlinks (source folder no longer exists)
for link in "$DEST_DIR"/*.md; do
  [ -e "$link" ] || continue
  [ -L "$link" ] || continue
  if [ ! -e "$link" ]; then
    rm -f "$link"
  fi
done

added=0
for dir in "$SOURCES_DIR"/*/; do
  name="$(basename "$dir")"
  src_md="$dir$name.md"
  dest_link="$DEST_DIR/$name.md"
  [ -f "$src_md" ] || continue
  if [ ! -e "$dest_link" ]; then
    ln -s "../../../wiki/sources/$name/$name.md" "$dest_link"
    added=$((added + 1))
  fi
done

echo "Synced sources for Quartz: $added new symlink(s), $(find "$DEST_DIR" -maxdepth 1 -name '*.md' | wc -l) total."
