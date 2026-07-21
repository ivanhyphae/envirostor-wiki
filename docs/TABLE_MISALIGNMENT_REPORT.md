# Markdown Table Misalignment: Diagnostic Report

**Date:** 2026-07-06  
**Author:** Automated scanner + manual analysis  
**Status:** Complete diagnostic; mitigation strategies drafted

---

## Summary

Marker OCR conversion of 141 PDFs produced **93 files with markdown tables (66%)**. Of these:

- **37 files (40%)** — well-formed, safe to use ✅
- **54 files (38%)** — wide tables (>10 columns), prone to OCR cell-merge errors ⚠️
- **2 files (2%)** — CRITICAL: both wide AND inconsistent cell counts 🚫

The two critical files have **poisoned** downstream LLM processing:
- `Draft Interim RACR_ App D-G.md` — 186 cells per line (!)
- `S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md` — 198 table blocks with cell count variance

**Bottom Line:** Without intervention, tables in these files will continue to generate spurious facts in wiki/concepts/ and primers.

---

## Root Cause

Marker converts table structure to markdown by preserving `|` pipe characters. OCR errors + column-width variance cause:

1. **Missing/extra pipes** within cells → cell count misalignment
2. **Stray pipes** from background grid noise → phantom cells
3. **No validation** → corrupted tables reach downstream consumers

Example (from GW report):
```
| MW-1 | 2012-05-01 | 12 | 15 | ND | 260 | (correct, 6 cells)
| MW-2 | 2012-05-01 | 14 | 16 || 80 |    (corrupt, 5 cells due to merged cell)
```

---

## Key Files

### 🔴 CRITICAL (Exclude from LLM)

| File | Max Cells | Blocks | Issue |
|------|-----------|--------|-------|
| Draft Interim RACR_ App D-G.md | 186 | 235 | Appendix; mostly specs/figures; unmanageable |
| S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md | 24 | 198 | GW monitoring data; critical for trends; inconsistent rows |

**Action:** Exclude from LLM processing. Source critical data from original PDF instead.

### 🟠 HIGH RISK (Wide Tables, >10 columns)

Top examples:
- `06A2542ct_TO97_GW Rpt_final.20230308.md` — 28 cells, 9 blocks (consolidated 2006–2023 GW)
- `7453_S9525-06-44_Modesto_Stockpiles_July_2012_GW_Report.1112.md` — 23 cells, 233 blocks (July 2012 GW)
- `S1200-01-01 Modesto Stockpiles GW April 2019_06.19.md` — 26 cells, 174 blocks (final GW round)
- `S1200-01-01 Modesto Stockpiles Jan 2018 SW Sampling_02.18.md` — 83 cells, 43 blocks (SW sampling)

**Action:** Flag for manual review; add inline validation warnings in wiki output.

### 🟢 LOW RISK (Well-formed)

37 files with small, clean tables:
- Contaminants primer ✅
- Compliance letters
- Memos and tech reports
- Approval correspondence

**Action:** Use as-is.

---

## Tools Provided

### 1. **`lib/scan_markdown_tables.py`** — Diagnostic Scanner

Scans all .md files in wiki/pdf2md/ and generates metrics.

```bash
python3 lib/scan_markdown_tables.py
```

**Output:** `raw/markdown_table_metrics.json` with file-by-file analysis.

**Use:** Run before each major wiki recompile to catch new problem files.

### 2. **`lib/table_guard.py`** — Processing Filter

Python module with functions to:
- `should_process_tables_in_file(filename)` — Returns False if file should skip tables
- `validate_table_block(rows)` — Check structural integrity
- `filter_markdown_content(content, filename)` — Strip tables if excluded
- `add_table_warning(content, filename)` — Add inline warnings

**Use:** Import into wiki compilation pipeline:

```python
from lib.table_guard import should_process_tables_in_file, filter_markdown_content

# Before passing markdown to LLM:
if not should_process_tables_in_file(filename):
    content = filter_markdown_content(content, filename)
else:
    # Optional: add warning if high-risk file
    content = add_table_warning(content, filename)
```

### 3. **`docs/TABLE_MISALIGNMENT_MITIGATION_STRATEGY.md`** — Full Strategy

4-phase implementation plan:
- Phase 1: Triage & documentation
- Phase 2: Guard rails (this week)
- Phase 3: High-value fixes (extract critical GW/SW tables from PDFs)
- Phase 4: Long-term (process improvement)

---

## Immediate Actions

### This Week

- [ ] Review this report with team
- [ ] Add table_metrics to `raw/envirostor_inventory.yaml`
- [ ] Integrate `table_guard.py` into wiki compilation pipeline
- [ ] Test: run wiki compile with excluded files; verify no poison tables

### Next Week

- [ ] For critical GW/SW tables: use Tabula or Camelot to extract from PDFs
- [ ] Create CSV versions of key groundwater monitoring tables
- [ ] Update primers to cite "data source: Table X, original PDF" where applicable

### Next Month

- [ ] Evaluate: can Marker's table settings be tuned for this corpus?
- [ ] Document table extraction process for future PDFs
- [ ] Train data-entry team on table validation

---

## How to Cite Data from Tables

**Before:** 
> "Barium concentrations ranged from 40–370 µg/L (GW Rpt_final.20230308.md)"

**After (if from excluded/high-risk file):**
> "Barium concentrations ranged from 40–370 µg/L ([2023 GW Monitoring Report](raw/06A2542ct_TO97_GW Rpt_final.20230308.pdf), Table 3)"

This way, readers can verify data against the original PDF if needed.

---

## Success Metrics

Once implemented, you should see:

1. ✅ No new "invented" numbers in wiki/concepts/ traceable to misaligned tables
2. ✅ All contaminant primers cite max values confirmed against original PDFs
3. ✅ GW/SW trend charts use validated data sources
4. ✅ User-facing docs note when data was OCR'd vs. manually extracted

---

## Questions & Escalation

- **"Is [specific file] safe to use?"** Check `raw/markdown_table_metrics.json` for severity classification
- **"Can I extract [table type] from a PDF?"** Yes, Tabula can handle most lab result tables; see Phase 3 mitigation strategy
- **"How do I add a new PDF?"** Run `scan_markdown_tables.py` after OCR conversion; flag if >10 columns

---

## Related Files

- `raw/markdown_table_metrics.json` — Complete diagnostic results
- `lib/table_guard.py` — Processing guard module
- `docs/TABLE_MISALIGNMENT_MITIGATION_STRATEGY.md` — Full 4-phase strategy

---

**Status:** Diagnostic complete; awaiting Phase 1 (triage) approval to proceed with mitigation.
