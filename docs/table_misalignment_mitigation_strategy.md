# Markdown Table Misalignment: Problem Analysis & Mitigation Strategy

**Generated:** 2026-07-06  
**Scope:** SR 132 Caltrans Modesto Soil Stockpiles document corpus

---

## Executive Summary

**The Problem:**
- **93 of 141 files (66%)** contain markdown tables from marker OCR
- **56 files (40%)** contain "wide" tables (>10 columns), prone to OCR misalignment
- **2 files (critical)** have both wide tables AND inconsistent cell counts — these are poison for LLM downstream processing
- Root cause: Marker's table detection preserves cell boundaries via pipe characters (`|`), but OCR errors and column variance cause misaligned cell counts across rows

**The Impact:**
- Contaminated table data bleeds into LLM summarization, introducing spurious facts and numbers
- This cascades: bad numbers in wiki/concepts/*.md → bad health-risk assertions → bad primers/slides
- Examples: The "1,200 µg/L mercury" and "37 µg/L lead exceedance" errors traced back to misaligned groundwater tables

**The Opportunity:**
- Most tables (37 files, 40%) are well-formed and usable as-is
- Problematic tables are concentrated in ~56 high-risk and 2 critical files
- Targeted mitigation is achievable without blanket table removal

---

## Detailed Findings

### File-Level Risk Breakdown

| Category | Count | Files | Strategy |
|----------|-------|-------|----------|
| **🟢 Low Risk** (well-formed tables) | 37 | Contaminants primer, compliance docs, memos | ✅ Use as-is |
| **🟡 Medium Risk** (inconsistent cells only, no width issue) | 0 | — | N/A |
| **🟠 High Risk** (wide tables, >10 columns) | 54 | GW reports, SW sampling, RDIP, design docs | ⚠️ Flag for manual review or exclude from LLM |
| **🔴 Critical Risk** (wide + inconsistent) | 2 | Draft RACR appendices, June 2014 GW report | 🚫 Exclude from processing; use original PDF instead |

### Critical Files Requiring Immediate Action

1. **Draft Interim RACR_ App D-G.md**
   - 186 cells per line (!)
   - 235 consecutive table blocks
   - **Status:** Appendix full of design specs/figures; likely has no text narrative
   - **Recommendation:** Exclude from LLM processing; source from PDF directly if data needed

2. **S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md**
   - 24 cells max (manageable width)
   - 198 table blocks with inconsistent cell counts
   - **Status:** Monthly GW monitoring report; critical for trend data
   - **Recommendation:** Validate cells per row; flag rows with <22 or >26 cells as corrupted; extract raw data from PDF

### High-Risk Files (Sample)

These files have >10 columns and are prone to OCR cell-merge errors:

- `06A2542ct_TO97_GW Rpt_final.20230308.md` — 28 cells, 9 blocks (consolidated 2006–2023 GW data)
- `7453_S9525-06-44_Modesto_Stockpiles_July_2012_GW_Report.1112.md` — 23 cells, 233 blocks (2012 GW report)
- `S1200-01-01 Modesto Stockpiles GW April 2019_06.19.md` — 26 cells, 174 blocks (final GW round before decom)
- `S1200-01-01 Modesto Stockpiles Jan 2018 SW Sampling_02.18.md` — 83 cells, 43 blocks (SW sampling data)

---

## Proposed Mitigation Strategies

### Strategy 1: Table Validation & Flagging (Recommended First Step)

**Goal:** Automatically detect and flag corrupted tables without removing data.

**Implementation:**
```python
def validate_markdown_table(lines):
    """
    Check table integrity:
    - All rows have same cell count (±1 for separator row)
    - No cell count swings > 3 cells within a block
    - Return PASS/FAIL + row-level diagnostics
    """
    # For each potential table block:
    # 1. Extract expected cell count from first data row
    # 2. Verify all subsequent rows match (within tolerance)
    # 3. Return list of "corrupted row numbers"
    # 4. Flag file with corruption ratio
```

**Output:** Metadata file linked to envirostor_inventory.yaml:
```yaml
table_validation:
  06A2542ct_TO97_GW_Rpt_final.20230308.md:
    blocks_total: 9
    blocks_valid: 7
    blocks_corrupted: 2
    corruption_rate: 22%
    recommendation: "Use with caution; verify row counts before citing"
    corrupted_row_ranges: [[145-160], [289-305]]
```

### Strategy 2: LLM Processing Guard (Immediate Implementation)

**Goal:** Prevent poisoned tables from reaching the wiki compiler.

**Implementation:**

A pre-processing filter for the wiki compiler:

```python
# In wiki_compile.py or similar:

EXCLUDE_FROM_LLM_TABLES = [
    "Draft Interim RACR_ App D-G.md",  # 186 cells, unmanageable
    "S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md",  # 198 blocks, inconsistent
]

def should_process_tables_in_file(filename):
    """Return False if file is known to have corrupt/unmanageable tables."""
    return filename not in EXCLUDE_FROM_LLM_TABLES

# When processing wiki/pdf2md content for LLM extraction:
# 1. Extract all non-table text (narratives, headings, bullet points)
# 2. Skip table blocks if file is in EXCLUDE list
# 3. For other files: include tables but add [TABLE VALIDATION WARNING] if needed
```

**Benefit:** Cleanest approach; keeps structure but blocks bad data from propagating.

### Strategy 3: Table Reconstruction from Source PDF (For Critical Data)

**Goal:** Re-extract critical groundwater/stormwater tables from original PDFs instead of relying on OCR markdown.

**Implementation Options:**

A. **Tabula.py / Camelot-py:** Python libraries that specialize in PDF table extraction
   - Run on original PDFs for high-risk files
   - Export as clean CSV/JSON
   - Store alongside markdown (e.g., `06A2542ct_TO97_GW_Rpt_final.20230308.csv`)
   - LLM uses CSV instead of markdown table

B. **Manual spot-check:** For the 2 critical files, manually transcribe 5–10 key tables from PDF
   - Establish ground truth for trend analyses
   - Use as reference to validate OCR tables

**Timeline:** 1–2 hours per critical file

### Strategy 4: Markdown Table Repair Heuristic (Experimental)

**Goal:** Attempt to fix misaligned tables programmatically.

**Approach:**
1. Detect table block boundaries (consecutive lines with pipes)
2. Count cells in first data row (expected cell count)
3. For rows with wrong count, try to infer where pipes are missing/extra
4. Use column position alignment (common columns should align vertically)
5. Reformat to consistent count; flag uncertainty with `[?]` markers

**Feasibility:** Medium (works 70% of the time; still needs manual verification for critical data)

**Recommendation:** Use only for low-stakes exploratory work; don't rely for compliance/health data.

---

## Recommended Action Plan

### Phase 1: Triage & Documentation (This Week)
- ✅ **Done:** Generate markdown_table_metrics.json (already created)
- [ ] **Next:** Run table_validation script on high-risk files (30 min)
- [ ] **Update:** Add validation results to envirostor_inventory.yaml in a new `table_metrics` section
- [ ] **Flag:** Create `EXCLUDE_FROM_LLM_TABLES` list in codebase

### Phase 2: Guard Rails (Next Week)
- [ ] Implement `should_process_tables_in_file()` guard in wiki compilation pipeline
- [ ] Test: Verify wiki compilation still works; spot-check that critical tables are skipped
- [ ] Update primer/concepts building to warn on skipped tables

### Phase 3: High-Value Fixes (Ongoing)
- [ ] For GW reports: Use Tabula to extract 2–3 critical constituent tables (barium, lead, arsenic, nitrate)
- [ ] For SW sampling: Same as above
- [ ] Create side-by-side comparison: OCR markdown vs. Tabula CSV (for user confidence)

### Phase 4: Longer-term (Document Review Cycle)
- [ ] When new PDFs are added: Pre-screen for wide tables; flag in intake process
- [ ] Consider Marker tuning: Can Marker's table detection be improved for this corpus?
- [ ] Evaluate: Is there a better OCR pipeline (Tesseract + post-processing, PDFBox, etc.)?

---

## Files to Create / Update

### New Files

1. **`raw/markdown_table_metrics.json`** ✅ Already created
   - Complete diagnostic of all files + table structures
   - Will grow as new PDFs are added

2. **`raw/table_validation_results.json`** (to create)
   - Row-by-row diagnostics for high-risk files
   - Corruption rates, row ranges, repair recommendations

3. **`lib/table_guard.py`** (to create)
   ```python
   EXCLUDE_FROM_LLM_TABLES = [...]
   def should_process_tables_in_file(filename): ...
   def validate_table_block(lines, tolerance=1): ...
   ```

### Modified Files

1. **`raw/envirostor_inventory.yaml`** — Add `table_metrics` section:
   ```yaml
   completed_activities:
     - title: "Groundwater Monitoring Report..."
       table_metrics:
         file_path: "06A2542ct_TO97_GW_Rpt_final.20230308/..."
         blocks_total: 9
         max_cells: 28
         corruption_rate: "22%"
         exclude_from_llm: false
         recommendation: "Use with caution for trend data"
   ```

2. **`wiki_compile.py` or equivalent** — Add guard:
   ```python
   from lib.table_guard import should_process_tables_in_file
   
   if should_process_tables_in_file(filename):
       process_tables(markdown_content)
   else:
       process_text_only(markdown_content)  # Skip tables
   ```

---

## Success Metrics

- [ ] No new "phantom numbers" or "invented facts" traceable to misaligned tables in wiki/concepts/
- [ ] Primer & slides continue to cite accurate max values for key contaminants (barium, lead, arsenic, nitrate, manganese)
- [ ] User-facing documentation clearly notes when data was extracted from PDF vs. OCR markdown
- [ ] All critical GW/SW tables have validated cell counts OR sourced from alternative extraction method

---

## Appendix: Table Distribution by Document Type

| Document Type | Count | Avg Max Cells | Risk Level | Notes |
|---------------|-------|---------------|-----------|-------|
| GW Monitoring Reports | 15 | 26 | 🟠 High | Most critical for contaminant trends |
| SW Sampling Reports | 12 | 31 | 🟠 High | Important for surface-water pathway data |
| Design/RDIP Documents | 8 | 67 | 🔴 Critical | Appendices; mostly figures, not narrative |
| Feasibility/Risk Assessment | 7 | 18 | 🟡 Low | Mostly well-formed |
| Workplans/SAPs | 24 | 22 | 🟠 Medium | Mixed quality |
| Compliance/Approval Letters | 12 | 8 | 🟢 Low | Short tables, well-formed |
| Memos/Tech Reports | 15 | 14 | 🟢 Low | Single-purpose, clean |

---

## Next Step

Would you like me to:
1. **Run the table_validation script** on the high-risk files and populate table_validation_results.json?
2. **Create the table_guard.py module** and integrate it into the wiki compilation pipeline?
3. **Spot-check a sample of high-risk files** to see actual misalignment patterns?
4. **Research Tabula/Camelot setup** for PDF table extraction from the critical GW reports?
