# Marker OCR Table Tuning Analysis

**Date:** 2026-07-06  
**Investigation:** Root cause of fragmented tables in GW monitoring reports

---

## Problem Diagnosis

### Symptom
File `S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md` contains **198 fragmented table blocks** instead of a coherent document with multiple related tables.

**Example fragmentation:**
```
Block 1: Lines 126–129 (Dissolved metals table)
  ↓ [5-line gap with heading]
Block 2: Lines 135–139 (Arsenic/Chromium/Vanadium table)
  ↓ [19-line gap with text]
Block 3: Lines 159–165 (More dissolved metals)
  ↓ [143-line gap with page break / section]
Block 4: Lines 309–312 (Figure caption)
  ↓ [1-line gap]
Block 5: Lines 314–323+ (Well monitoring data table — 150+ rows)
...continues for 198 blocks total
```

### Root Cause
The PDF structure (164 pages, print-protected, copy-disabled) contains **legitimate content fragments** — monthly monitoring tables for different wells and constituents. Marker is correctly detecting each table, but **not merging adjacent or logically-related tables** that should be seen as a continuous dataset.

This is NOT a cell-alignment issue (pipes are consistent within each block). Instead, it's a **table context fragmentation** issue.

---

## Marker's Table Processors

Marker has **two table-related LLM processors**:

### 1. `LLMTableProcessor`
- Detects and converts individual table regions
- Settings: max rows, OCR quality, iteration limits
- **Status:** Working correctly for this corpus

### 2. `LLMTableMergeProcessor` ⚙️ **KEY**
- Merges adjacent or nearby tables on same page / across pages
- **Currently NOT active or undertuned for this corpus**
- Parameters to adjust:

| Parameter | Purpose | Default | Recommendation |
|-----------|---------|---------|-----------------|
| `vertical_table_distance_threshold` | Max gap between vertically-stacked tables to merge | ? | Lower (e.g., 50→20 pixels) |
| `vertical_table_height_threshold` | Height tolerance for vertical merge | ? | Tighten |
| `table_height_threshold` | Min height ratio (rel. to page) for first table | ? | Adjust |
| `table_start_threshold` | Max % down page for second table to merge | ? | Increase (e.g., 0.8→0.9) |
| `no_merge_tables_across_pages` | Disable cross-page merging | False | Keep False (we want merging) |

---

## Current Configuration

**File:** `marker-config.json`

```json
{
  "llm_service": "marker.services.openai.OpenAIService",
  "openai_api_key": "...",
  "openai_base_url": "https://openrouter.ai/api/v1",
  "openai_model": "google/gemini-3.1-flash-lite",
  "use_llm": true,
  "timeout": 360,
  "max_retries": 5,
  "retry_wait_time": 10
}
```

**Missing:** No table-specific tuning parameters. Using Marker's defaults for table merging.

---

## Proposed Solution

### Option A: Aggressive Table Merging (Recommended)

Add table-merge parameters to marker-config.json or process-pdfs.sh:

```bash
# Add to process-pdfs.sh marker command:
--LLMTableMergeProcessor_vertical_table_distance_threshold 30 \
--LLMTableMergeProcessor_vertical_table_height_threshold 0.1 \
--LLMTableMergeProcessor_table_height_threshold 0.05 \
--LLMTableMergeProcessor_table_start_threshold 0.85 \
```

**Expected outcome:**
- Adjacent tables with <30px gap → merged
- Tables on same page → merged if start position close
- Reduces 198 blocks → ~50–100 coherent tables per report

**Trade-off:** May over-merge unrelated tables (requires testing on sample).

### Option B: Reprocessing with Extended Config

Create a new config file:

**File:** `marker-config-aggressive-merge.json`

```json
{
  "llm_service": "marker.services.openai.OpenAIService",
  "openai_api_key": "...",
  "openai_base_url": "https://openrouter.ai/api/v1",
  "openai_model": "google/gemini-3.1-flash-lite",
  "use_llm": true,
  "timeout": 360,
  "max_retries": 5,
  "retry_wait_time": 10,
  "LLMTableMergeProcessor": {
    "vertical_table_distance_threshold": 30,
    "vertical_table_height_threshold": 0.1,
    "table_height_threshold": 0.05,
    "table_start_threshold": 0.85
  }
}
```

Usage:
```bash
./process-pdfs.sh --reprocess --config-json marker-config-aggressive-merge.json
```

**Benefit:** Non-destructive; can test on a few files before full reprocessing.

---

## Test Plan

### Phase 1: Single-File Validation
1. Reprocess ONE file with aggressive merge settings:
   ```bash
   marker /tmp/test-pdf \
     --output_dir /tmp/test-output \
     --config_json marker-config-aggressive-merge.json
   ```
2. Compare fragment count:
   - Before: 198 table blocks
   - Expected after: 50–100 blocks
   - Check for over-merging (unrelated tables merged)

3. Spot-check table integrity:
   - Pick 5 tables from output
   - Verify cell counts are consistent
   - Manually verify against PDF if uncertain

### Phase 2: Multi-File Batch
1. Reprocess all GW monitoring reports (15 files)
2. Run diagnostic scanner on output
3. Check: wide table count, inconsistent cells, fragmentation ratio

### Phase 3: Full Reprocessing
1. If Phase 2 passes, reprocess entire corpus with new config
2. Re-run wiki compilation
3. Verify no new "phantom numbers" in wiki/concepts/

---

## Open Questions

1. **What are the current defaults for table merge parameters?**
   - Would help us understand why merging isn't happening
   - Marker docs don't list defaults explicitly

2. **Can we tune merge parameters per-processor priority?**
   - I.e., should LLMTableMergeProcessor run before or after TableProcessor?
   - Might affect fragmentation

3. **Is `use_llm: true` being applied to table processors?**
   - Does the Gemini model help with table structure understanding?
   - Or does it need explicit `--LLMTableProcessor_use_llm` flag?

---

## Sage-wiki Integration Opportunity

**If Marker tuning isn't sufficient**, this reveals a good feature request for sage-wiki:

**Proposal:** Add table validation/merging to the sage-wiki markdown → concept compilation pipeline.

```go
// In sage-wiki's markdown parser:
if detectFragmentedTables(markdown) {
    merged := mergeAdjacentTables(markdown)
    // Log warning: "Found 198 fragments, merged to N tables"
    return merged
}
```

This would be a **general-purpose improvement** for any sage-wiki user working with Marker-converted PDFs (which is probably common in regulatory/environmental docs).

---

## Recommendation

**Immediate next step:** Test Option A on one critical file:

```bash
# Re-extract one problem file with table merge tuning
/home/ivanh/.venvs/surya/bin/marker \
  /path/to/raw/S9800-01-17*.pdf \
  --output_dir /tmp/test-marker-output \
  --config_json marker-config.json \
  --LLMTableMergeProcessor_vertical_table_distance_threshold 30 \
  --LLMTableMergeProcessor_table_start_threshold 0.85
```

Compare output:
```bash
python3 lib/scan_markdown_tables.py /tmp/test-marker-output
```

If fragment count drops significantly AND tables remain well-formed, we've found the fix.

---

## References

- Marker CLI help: `/home/ivanh/.venvs/surya/bin/marker --help`
- Table processor docs: Search for `LLMTableMergeProcessor` in help output
- Current config: `marker-config.json`
- Process script: `process-pdfs.sh`
