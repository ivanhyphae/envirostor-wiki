#!/usr/bin/env bash
# PDF text extractor using pdftotext (poppler).
# sage-wiki passes the raw file bytes on stdin.
# Writes extracted plain text to stdout.
#
# Notes:
# - No -layout flag: layout mode pads tabular content with huge amounts of
#   horizontal whitespace that inflates token counts 2-16x with no benefit
#   to the LLM. Linear extraction is cleaner for regulatory documents.
# - 120K char cap: prevents the synthesis step from receiving overwhelming
#   input when chunking very large PDFs. The first 120K chars of a monitoring
#   report contain all the header, background, findings, and key data tables.
set -euo pipefail

tmp=$(mktemp /tmp/sage-pdf-XXXXXX.pdf)
trap 'rm -f "$tmp"' EXIT

cat > "$tmp"
pdftotext -enc UTF-8 "$tmp" - | head -c 120000
