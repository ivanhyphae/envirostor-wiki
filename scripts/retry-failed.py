#!/usr/bin/env python3
"""
Prepare for a clean retry of failed and hollow-summary sources.

Two problems are fixed:
  1. Sources that failed at the LLM stage are not in the manifest at all,
     so they will be picked up as new files on the next compile automatically.
  2. Sources that "compiled" but produced hollow summaries (extraction failure)
     ARE in the manifest and must be removed so the diff sees them as new.

This script removes known hollow-summary sources from .manifest.json.
Run it, then run: sage-wiki compile
"""
import json, os, pathlib, sys

project_dir = pathlib.Path(__file__).resolve().parent.parent
manifest_path = project_dir / ".manifest.json"
summaries_dir = project_dir / "wiki" / "summaries"

HOLLOW_MARKERS = [
    "not extractable",
    "no text",
    "binary metadata",
    "linearized",
    "content stream",
    "no data",
    "cannot report",
    "cannot be determined",
    "encrypted",
    "compressed or encoded",
    "not readable",
    "no readable",
    "unreadable",
]

with open(manifest_path) as f:
    manifest = json.load(f)

# Find summaries with hollow content
hollow_sources = []
for md_file in sorted(summaries_dir.glob("*.md")):
    text = md_file.read_text(errors="replace").lower()
    if any(marker in text for marker in HOLLOW_MARKERS):
        # Extract source path from frontmatter
        for line in md_file.read_text(errors="replace").splitlines():
            if line.startswith("source:"):
                src = line.split("source:", 1)[1].strip()
                hollow_sources.append(src)
                break

if not hollow_sources:
    print("No hollow summaries found — nothing to do.")
    sys.exit(0)

print(f"Found {len(hollow_sources)} hollow summaries to requeue:")
removed = []
for src in hollow_sources:
    print(f"  {src}")
    if src in manifest.get("sources", {}):
        del manifest["sources"][src]
        removed.append(src)
    else:
        print(f"    (not in manifest — will be picked up automatically)")

# Also delete the hollow summary files so they get freshly written
for md_file in sorted(summaries_dir.glob("*.md")):
    text = md_file.read_text(errors="replace").lower()
    if any(marker in text for marker in HOLLOW_MARKERS):
        md_file.unlink()
        print(f"  deleted hollow summary: {md_file.name}")

if removed:
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nRemoved {len(removed)} entries from manifest.")

state_path = project_dir / ".sage" / "compile-state.json"
if state_path.exists():
    with open(state_path) as f:
        state = json.load(f)
    failed = [e["path"] for e in (state.get("failed") or [])]
    if failed:
        print(f"\n{len(failed)} LLM-failed sources not in manifest — will retry automatically:")
        for p in failed:
            print(f"  {p}")

print("\nRun: sage-wiki compile")
