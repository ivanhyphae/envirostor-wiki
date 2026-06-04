---
concept: epa-method-6020-7470
entity_type: technique
aliases: ["epa 6020", "epa 7470"]
sources: ["raw/S9800-01-17 Caltrans Modesto Stockpiles GW_06.15.pdf"]
confidence: medium
created_at: 2026-06-04T08:26:59Z
---

## Definition

**EPA Method 6020** (Inductively Coupled Plasma – Mass Spectrometry, ICP-MS) is an analytical procedure for the determination of trace elements, including metals and selected non‑metals, in aqueous samples and solid wastes following appropriate digestion. **EPA Method 7470** is a cold‑vapor atomic absorption (CVAA) method specifically for the analysis of total mercury in liquid wastes (e.g., groundwater, process waters). Together, these methods are often cited in environmental compliance monitoring, where Method 6020 covers a wide suite of metals and Method 7470 provides the required low‑level mercury analysis.

## How it works

### Method 6020 (ICP‑MS)
1. **Sample preparation:** Aqueous samples are typically acid‑digested (e.g., with nitric acid) to dissolve metals and reduce interferences. Solid samples undergo a separate digestion procedure (e.g., EPA Method 3050 or 3051) before analysis.
2. **Instrumentation:** An inductively coupled plasma (argon plasma at ~6000–10000 K) atomizes and ionizes the sample. Ions are extracted into a mass spectrometer (usually a quadrupole or sector‑field).
3. **Detection:** Ions are separated by mass‑to‑charge ratio (m/z) and counted with an electron multiplier. Calibration uses multi‑element standards, typically with internal standards (e.g., Sc, Ge, In, Bi) to correct for matrix effects and drift.
4. **Data reporting:** Concentrations are reported in µg/L (ppb) or mg/L (ppm). Method 6020 achieves detection limits in the sub‑ppb range for most elements.

### Method 7470 (Cold‑Vapor Atomic Absorption)
1. **Sample preparation:** Aqueous samples are digested with a strong oxidizer (e.g., potassium permanganate / persulfate) to convert all forms of mercury to Hg²⁺. Excess oxidizer is reduced with hydroxylamine hydrochloride.
2. **Reduction to elemental mercury:** Stannous chloride (SnCl₂) is added to the digested sample, reducing Hg²⁺ to volatile elemental mercury (Hg⁰).
3. **Purge and trap:** An inert gas (argon or nitrogen) purges the Hg⁰ from the solution; the vapor is passed through a gold trap or directly into an absorption cell.
4. **Detection:** Atomic absorption at 253.7 nm is measured. The absorption signal is proportional to mercury concentration. The method detection limit is typically ≤ 0.2 µg/L.

## Variants

- **Method 6020A / 6020B:** Later updates to the original 6020 include refinements in spectral interference correction (e.g., using collision/reaction cells) and expanded analyte lists.
- **Method 7470A:** The “A” revision (SW‑846 Update III) clarifies reagent specifications and quality control procedures, but the core chemistry remains the same.
- **Hyphenated methods:** For speciated mercury analysis, Method 6020 can be coupled to a mercury‑specific detection system, though EPA 1630 (methyl mercury) or 1631 (total mercury by CVAFS) are more common for low‑level mercury.
- **Alternative to 7470:** Method 1631 (cold‑vapor atomic fluorescence, CVAFS) offers lower detection limits and is often preferred for pristine waters; Method 7471 is the counterpart for solid wastes.

## Trade-offs

- **Method 6020:**  
  - *Advantages:* Multi‑element capability (40+ analytes per run), high sensitivity, isotopic ratio information possible.  
  - *Limitations:* High capital and maintenance cost; susceptibility to polyatomic interferences (e.g., ArCl⁺ on As, CaO⁺ on Fe); requires careful matrix matching; cannot analyze mercury directly because of memory effects and low ionization efficiency.

- **Method 7470:**  
  - *Advantages:* Relatively simple, low‑cost instrumentation; excellent selectivity and sensitivity for mercury.  
  - *Limitations:* Single‑element only; requires thorough digestion to avoid loss of volatile mercury; lower throughput than ICP‑MS for multi‑element work; detection limits are higher than Method 1631.

- **Combined use in compliance monitoring:** Laboratories often use Method 6020 for routine metals and Method 7470 for mercury to meet reporting limits for groundwater, as specified in NPDES permits or RCRA waste characterization. The two methods can be run from the same sample preparation (if the digestion is compatible), but mercury analysis typically requires a separate digestion and instrument.

## See also

- EPA Method 3050B (Acid digestion of sediments, sludges, and soils)
- EPA Method 1631 (Total mercury in water by CVAFS)
- Inductively Coupled Plasma Mass Spectrometry
- Cold Vapor Atomic Absorption Spectroscopy
- SW-846 Test Methods for Evaluating Solid Waste
- Groundwater Monitoring