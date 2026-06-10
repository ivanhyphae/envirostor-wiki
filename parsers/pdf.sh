#!/usr/bin/env bash
# PDF text extractor using pdftotext (poppler).
# sage-wiki passes the raw file bytes on stdin.
# Writes extracted plain text to stdout.
set -euo pipefail

tmp=$(mktemp /tmp/sage-pdf-XXXXXX.pdf)
trap 'rm -f "$tmp"' EXIT

cat > "$tmp"
pdftotext -layout -enc UTF-8 "$tmp" -
