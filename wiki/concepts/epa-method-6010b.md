---
concept: epa-method-6010b
entity_type: technique
aliases: ["EPA 6010B", "ICP-AES", "EPA Method 6010B"]
sources: ["raw/SR 132 Basin 5 Clean Fill Tech Memo revised 7-2-2020.pdf", "raw/Stockpile 2 MSE Wall Sampling Tech Memo.pdf", "raw/7084_S9525-06-44 Response to DTSC Workplan Comments.0912.pdf"]
confidence: medium
created_at: 2026-06-04T03:25:00Z
---

## Definition

**EPA Method 6010B** is a U.S. Environmental Protection Agency (EPA) analytical procedure for the determination of trace elements (metals and metalloids) in aqueous samples, waste extracts, and solid wastes using inductively coupled plasma atomic emission spectrometry (ICP‑AES). It is part of the SW‑846 “Test Methods for Evaluating Solid Waste” series and was originally published as Revision B in 1996. The method is widely used for compliance monitoring, site characterization, and waste classification (e.g., clean fill assessment) due to its multi‑element capability and moderate cost.

## How it works

The method employs ICP‑AES, where a peristaltic pump delivers a liquid sample (typically after acid digestion or filtration) to a nebulizer. The resulting aerosol is injected into an argon plasma sustained at 6000–10000 K, causing atomization and ionization of analytes. Emitted light of characteristic wavelengths is measured by either a sequential scanning monochromator or a simultaneous polychromator. Calibration is performed using multi‑element standard solutions, and quantitation is based on the intensity of the emission line relative to the calibration curve.

Key procedural steps include:
1. **Sample preparation**: Aqueous samples are filtered (0.45 µm) and acidified; solid wastes are digested according to methods 3050B, 3051, or 3052. Extractable elements are measured after preparation such as Toxicity Characteristic Leaching Procedure (TCLP) extract.
2. **Instrument setup**: Plasma conditions (power, gas flow rates), wavelength selection, and background correction are optimized for each analyte.
3. **Analysis**: Samples are aspirated in triplicate, and interference checks (spectral, matrix, drift) are performed. Quality control includes initial calibration verification (ICV), continuing calibration verification (CCV), blank, and spike samples.
4. **Data handling**: Concentrations are calculated from emission intensity, corrected for background and interferences, and reported with appropriate detection limits.

The method covers numerous elements, including but not limited to: aluminum, antimony, arsenic, barium, beryllium, cadmium, calcium, chromium, cobalt, copper, iron, lead, magnesium, manganese, molybdenum, nickel, potassium, selenium, silver, sodium, thallium, vanadium, and zinc.

## Variants

EPA Method 6010 has undergone several revisions, each refining quality control requirements and expanding analyte lists:

- **6010A (1992)**: Original SW‑846 version.
- **6010B (1996)**: Introduced tighter QC, defined interference checks, and specified background correction.
- **6010C (2007)**: Updated to reflect modern ICP‑AES instrumentation (e.g., simultaneous polychromators, charge‑coupled devices), and allowed use of axial‑view plasma for improved sensitivity.
- **6010D (2014)**: Current revision; adds guidance on collision/reaction cells (though primarily used in ICP‑MS), describes alternative sample introduction techniques (e.g., ultrasonic nebulization), and formalizes detection limit calculations.

Parallel methods include:
- **EPA Method 6020 (ICP‑MS)**: Lower detection limits, isotope ratio capability, but higher cost and more complex interferences.
- **EPA Method 7000 series (Flame AA)**: Single‑element, less expensive, but with higher detection limits and slower multi‑element throughput.

## Trade-offs

| Advantage | Limitation |
|-----------|------------|
| Simultaneous multi‑element detection (up to ~30 elements) | Higher detection limits than ICP‑MS (low‑ppb vs. sub‑ppb) |
| Moderately low cost per element after initial investment | Spectral interferences (e.g., arsenic at 193.7 nm from aluminum) requiring correction |
| Robust for high‑total‑dissolved‑solids (TDS) matrices | Matrix effects (viscosity, ionization) that demand dilution or internal standardization |
| Widely accepted by regulatory agencies (RCRA, CERCLA) | Sample preparation (digestion) can be time‑consuming and prone to loss of volatile elements (e.g., selenium, arsenic) |
| Automated operation and rapid analysis | Calibration drift over long runs; requires frequent QC checks |

Specific to environmental applications (e.g., clean fill characterization as referenced in the provided documents), Method 6010B is often used to verify that contaminants (lead, arsenic, chromium, etc.) are below regulatory thresholds. However, for very low‑level detection (sub‑ppb), ICP‑MS (Method 6020) is preferred.

## See also

- EPA Method 6010C
- EPA Method 6020
- Inductively coupled plasma atomic emission spectroscopy
- SW-846
- EPA Method 3050B
- Toxicity Characteristic Leaching Procedure