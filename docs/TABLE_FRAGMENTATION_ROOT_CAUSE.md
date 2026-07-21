# Table Fragmentation Root Cause Analysis

**Date:** 2026-07-06  
**Focus:** Understanding why Marker produces 198 fragmented table blocks for the June 2014 GW report

---

## Problem Statement

File `S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md` (5,053 lines):
- **Expected:** A coherent document with ~30–50 distinct monitoring tables
- **Actual:** 198 separate table fragments with inconsistent cell counts
- **Impact:** Downstream LLM processing sees fragmented data → spurious aggregations in wiki/concepts/

---

## Not a Cell-Alignment Issue

Our diagnostic scanner confirmed that cells ARE consistent WITHIN each table block:

```markdown
✅ Table Block 1 (lines 126–129):
| Dissolved Metal  | High Concentration | Low Concentration | Numeric Water Quality Threshold |
| Barium (µg/l)    | 280 (MW-5)         | 51 (MW-3)         | 1,000 / 700                     |
| Strontium (µg/l) | 1,100 (MW-1)       | 250 (MW-8)        | 4,000                           |
✅ 4 cells per row, consistent pipe structure

✅ Table Block 2 (lines 135–139):
| Dissolved Metal | High Concentration | Low Concentration | Numeric Water Quality Threshold |
| Arsenic (μg/l)  | 4.5 (MW-3)        | 1.1 (MW-1)        | 10                              |
| Chromium (μg/l) | 8.3 (MW-6)        | 1.6 (MW-10)       | 50                              |
✅ 4 cells per row, consistent pipe structure
```

The issue is FRAGMENTATION: related tables aren't merged even though they sit 5–10 lines apart on the same page.

---

## Root Cause: LLMTableMergeProcessor Undertuned

Marker has two table processors:

| Processor | Role | Status |
|-----------|------|--------|
| **LLMTableProcessor** | Detects and OCRs individual table regions | ✅ Working correctly |
| **LLMTableMergeProcessor** | Merges adjacent tables on same/adjacent pages | ⚠️ **Undertuned or not active** |

The merge processor exists in Marker's codebase but either:
1. Isn't enabled by default, or
2. Uses overly conservative default parameters

**Evidence:** The GW report has legitimate separate tables (monthly data for different wells/parameters), but they should be grouped by logical context. The current fragmentation obscures the document structure.

---

## Tuning Strategy

### Key Parameters

| Parameter | Purpose | Default | Proposed |
|-----------|---------|---------|----------|
| `vertical_table_distance_threshold` | Max gap (pixels) between vertically-stacked tables to merge | Unknown | 30 |
| `vertical_table_height_threshold` | Height ratio tolerance for vertical merge | Unknown | 0.1 |
| `table_height_threshold` | Min height ratio (rel. to page) for first table | Unknown | 0.05 |
| `table_start_threshold` | Max position (% down page) for second table to merge | Unknown | 0.85 |

### Rationale

**Lower distance threshold (20–30 px):** Tables separated by headings/subtext (a few lines) should merge.  
**Higher position threshold (0.85):** Be more aggressive about merging tables that span most of a page.  
**Lower height thresholds:** Reduce filtering; allow merge of differently-sized tables (e.g., summary + detail).

### Expected Outcome

- **Fragment count:** 198 blocks → ~50–80 coherent tables
- **Cell consistency:** Stable within merged blocks
- **Over-merging risk:** Unrelated tables might incorrectly merge (requires visual inspection)

---

## Why This Matters

### For This Project
The June 2014 GW report is critical for remediation assessment. Currently:
- 198 fragments make automated analysis impossible
- Each LLM pass on wiki compilation re-synthesizes the same data in different ways
- Results: inconsistent contaminant levels, phantom correlations in concept graph

### For Marker Upstream
If tuning works, this is a **general-purpose fix for regulatory/environmental PDFs**, which commonly have:
- Repeated table structures across many pages
- Natural logical groupings (monthly reports, parameter types)
- Limited contextual hints for table association

Worth submitting as:
- Issue: "Aggressive table merging doesn't activate in regulatory documents"
- PR: Proposed default parameters or auto-detection logic

---

## Testing Plan

### Current Run
1. Reprocess June 2014 GW report with aggressive merge parameters
2. Run diagnostic scanner on output
3. Spot-check 5–10 tables for:
   - Cell count consistency within merged blocks
   - No over-merging of unrelated tables
   - Data integrity (spot-check values against PDF)

### Decision Criteria

✅ **SUCCESS** (apply to full corpus):
- Fragment count reduces by >50% (198 → <100)
- Cell counts remain consistent
- Spot-checks pass

⚠️ **PARTIAL** (need refinement):
- Fragment count reduces by 20–50%
- Some over-merging visible
- → Adjust parameters and retry

❌ **FAILURE** (pivot strategy):
- No change in fragment count
- Merge processor not activating
- → Document as limitation; pursue pre-processing or sage-wiki feature request

---

## Files Involved

- **Test input:** `/tmp/marker-test-input/S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf` (3.8 MB, 164 pages)
- **Baseline output:** `wiki/pdf2md/S9800-01-17.../S9800-01-17....md` (5,053 lines, 198 fragments)
- **Diagnostic tool:** `lib/scan_markdown_tables.py`
- **Config:** `marker-config.json` (tuning params passed via CLI)

---

## Next Steps

**Once test completes:**

1. Run diagnostic scanner on test output
   ```bash
   python3 lib/scan_markdown_tables.py /tmp/marker-test-output
   ```

2. Compare metrics:
   - Table block count: 198 → ?
   - Max cells/line: 24 → ?
   - Cell consistency: INCONSISTENT → CONSISTENT?

3. Manual spot-check:
   - Pick 3–5 tables from test output
   - Compare against original PDF
   - Verify no spurious merges

4. Decision:
   - If >50% reduction & quality OK → recommend for full corpus
   - If partial → document findings & prepare sage-wiki feature request
   - If no change → escalate to Marker maintainers

---
