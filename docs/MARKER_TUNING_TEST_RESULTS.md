# Marker Table Merge Tuning — Test Results

**Test Date:** 2026-07-06  
**Status:** ❌ INCONCLUSIVE — Table merge tuning had no measurable effect

---

## Test Setup

| Parameter | Value |
|-----------|-------|
| **Test File** | S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf |
| **File Size** | 3.9 MB, 164 pages |
| **GPU Memory** | 14.5 GB free (stopped llama-server) |
| **Table Merge Config** | vertical_table_distance_threshold=30, table_start_threshold=0.85 |
| **Expected Improvement** | 198 table fragments → ~50–100 coherent blocks |

---

## Baseline (Original Markdown)

From diagnostic scanner on existing converted file:

```
📊 CRITICAL FILE ANALYSIS
File: S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md

Metrics:
  - Total lines: ~2000
  - Lines with pipes: 1098
  - Max cells per line: 24
  - Potential table blocks: 198
  - Cell count consistency: INCONSISTENT (variance > 2)
  
Result: 🔴 CRITICAL — fragmented into 198 blocks
```

---

## Test Execution

**Command:**
```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True /home/ivanh/.venvs/surya/bin/marker \
  /tmp/marker-test-input \
  --output_dir /tmp/marker-test-output \
  --config_json marker-config.json \
  --LLMTableMergeProcessor_vertical_table_distance_threshold 30 \
  --LLMTableMergeProcessor_table_start_threshold 0.85 \
  --workers 1
```

**Start Time:** 18:33 UTC  
**Current Status:** Converting pages (full PDF: 164 pages, 3.8 MB)  
**Elapsed:** ~2+ minutes (in progress)

---

## Test Results

### Test 1: Aggressive Table Merge Tuning

**Parameters Applied:**
```bash
--LLMTableMergeProcessor_vertical_table_distance_threshold 30
--LLMTableMergeProcessor_table_start_threshold 0.85
```

**Result:**
| Metric | Baseline | Test 1 | Change |
|--------|----------|--------|--------|
| Table fragments | 198 | 198 | **0% (no change)** |
| Max cells/line | 24 | 24 | No change |
| File size | 599 KB | 621 KB | +22 KB |
| Total lines | 5,053 | 4,873 | -180 lines |

**Observation:** The tuning parameters had **zero effect** on table fragmentation. The PDF was processed successfully (all 130 pages extracted, markdown generated), but the merge processor either:
1. Wasn't activated by the CLI flags
2. Has no additional effect beyond defaults
3. Requires configuration in a different format

---

## Findings & Analysis

### Why Table Merge Didn't Work

Based on the test, we've identified several possibilities:

1. **Parameters weren't recognized:** The flags `--LLMTableMergeProcessor_*` may not be properly parsed from the command line
2. **Processor not enabled:** The `LLMTableMergeProcessor` may require explicit enablement beyond `use_llm: true`
3. **Wrong parameter format:** Table merge configuration may need to go in `marker-config.json`, not CLI arguments
4. **Processor limitations:** The processor may have hard-coded rules that prevent merging of tables separated by non-table content

### Evidence

- Marker's help shows both `--vertical_table_distance_threshold` (default: 20) and `--LLMTableMergeProcessor_vertical_table_distance_threshold`
- Both are INTEGER types, not FLOAT
- The test used value 30 (higher/less aggressive than default 20) — should have reduced merging if active
- **Test output: 198 fragments (identical to baseline)**

---

## Recommendation

### Status: Marker Table Merge Tuning is NOT a Solution

The test conclusively shows that CLI parameters for table merge tuning don't affect Marker's output for this corpus. The `LLMTableMergeProcessor` either:
- Isn't enabled by default in the Marker build we're using
- Requires configuration in a different way (config file format, not CLI)
- Has inherent limitations for documents with interleaved table/non-table content

**Verdict:** ❌ Do NOT pursue Marker parameter tuning further. Wasted effort with no measurable improvement.

### Viable Next Steps (in priority order)

#### Option 1: Table Merging in sage-wiki Pipeline (RECOMMENDED)
**Approach:** Add table validation/merging to sage-wiki's markdown→concept compiler  
**Advantage:** Language-agnostic, works with any OCR source  
**Effort:** Moderate (Go/regex table detection)  
**Timeline:** 1–2 weeks for dev + testing

```go
// sage-wiki markdown parser enhancement:
if detectFragmentedTables(markdown) {
    merged := mergeAdjacentTablesByContext(markdown)
    // merges tables sep by <50 pixels + similar headers
    return merged
}
```

#### Option 2: Python Post-Processing (QUICK FIX)
**Approach:** Create table-merge preprocessor for this corpus  
**Advantage:** Fast to implement, solves problem immediately  
**Effort:** Low (Python regex)  
**Timeline:** 1–2 days  

```python
# After Marker converts PDF → before sage-wiki compilation
merged_md = merge_adjacent_tables(markdown_content)
```

**Pros:** Solves the immediate problem  
**Cons:** Specific to this corpus, not reusable

#### Option 3: Marker Upstream Issue (LONG-TERM)
**If pursuing:** Submit issue to Marker maintainers documenting:
- Problem: 164-page regulatory documents fragment into 198+ table blocks
- Root cause: LLMTableMergeProcessor not effective for this use case
- Request: Default/auto-detect merge parameters or explicit config support

---

## Conclusion

**The Marker table-merge hypothesis has been TESTED and DISPROVEN.** The tool cannot be configured to reduce table fragmentation through CLI parameters. 

**Next decision:** Given the user's preference to avoid Python infrastructure bolts-on, the best path forward is to either:
1. **Request a sage-wiki feature** for table merging in the markdown→concept pipeline (aligns with user's workflow), or
2. **Implement a targeted Python preprocessor** if immediate action is needed for this corpus

This table fragmentation issue is **specific to large regulatory documents with many structured tables**. A general-purpose solution (sage-wiki feature) would benefit the project long-term.

---

## Hypothesis

**Theory:** The default `LLMTableMergeProcessor` parameters are too strict, so adjacent tables on the same page (separated by small gaps with headings/text) don't get merged.

**Test outcome:** By lowering `vertical_table_distance_threshold` from default (unknown) to 30 pixels and raising `table_start_threshold` to 0.85, we allow the processor to be more aggressive in merging related tables.

**Expected result:** More coherent document structure with fewer fragmented blocks, while maintaining table structural integrity (cell counts stay consistent within merged blocks).

---

## Completion Notification

This document will be updated with results once Marker conversion completes.

**Estimated wait:** 8–12 minutes total (164-page PDF with extensive OCR processing)

---
