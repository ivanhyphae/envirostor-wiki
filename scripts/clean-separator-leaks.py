#!/usr/bin/env python3
"""
Clean up marker PDF output: replace separator leaks and strip inline base64 images.

1. Lines >10,000 chars that are >90% dashes/pipes/whitespace → replace with ---
2. Inline base64-encoded images anywhere in any line → remove the data URI
"""

import glob
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF2MD = os.path.join(REPO, "wiki", "pdf2md")

LINE_THRESHOLD = 10_000
DASH_RATIO = 0.90

# Matches data:image/{format};base64,{base64_data}
# The base64 payload can be huge so we match up to the next quote or whitespace
B64_RE = re.compile(
    r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+',
    re.IGNORECASE,
)

results = {
    "scanned": 0,
    "separator_lines": 0,
    "b64_images_removed": 0,
    "skipped_wide_tables": 0,
}

for md_file in sorted(glob.glob(os.path.join(PDF2MD, "*", "*.md"))):
    results["scanned"] += 1

    with open(md_file, encoding="utf-8", errors="replace") as f:
        original = f.read()

    lines = original.split("\n")
    changed = False
    new_lines = []

    for line in lines:
        # Phase 1: strip inline base64 images (runs before length check)
        b64_found = B64_RE.findall(line)
        if b64_found:
            line = B64_RE.sub("", line)
            results["b64_images_removed"] += len(b64_found)
            changed = True

        # Phase 2: handle separator leaks (only makes sense after b64 removal)
        if len(line) > LINE_THRESHOLD:
            noncontent = sum(1 for c in line if c in "-| \t")
            ratio = noncontent / len(line)

            if ratio > DASH_RATIO:
                new_lines.append("---")
                changed = True
                results["separator_lines"] += 1
            else:
                new_lines.append(line)
                results["skipped_wide_tables"] += 1
        else:
            new_lines.append(line)

    if changed:
        new_content = "\n".join(new_lines)
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        short = os.path.relpath(md_file, PDF2MD)
        print(f"  CLEANED: {short}")

print(
    f"\nDone: {results['scanned']} files scanned, "
    f"{results['separator_lines']} separator lines replaced, "
    f"{results['b64_images_removed']} base64 images stripped, "
    f"{results['skipped_wide_tables']} wide-table lines left alone."
)