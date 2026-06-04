---
concept: total-dissolved-solids
entity_type: concept
aliases: ["TDS"]
sources: ["S9525-01-44B Modesto Stockpiles GW June 2013.0613.pdf", "S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf", "raw/S2350-01-02 Updated Statistical Evaluation Report_2.24.pdf", "raw/S9525-06-44AModesto Stockpiles GW SEPT2012 1212.pdf", "raw/S9800-01-17 Modesto Stockpiles Feb2014 GW Mon 0414 (1).pdf", "raw/S2350-01-02_2.4.2025 Stormwater Sampling Report_6.25.pdf"]
confidence: high
created_at: 2026-06-04T08:17:39Z
---

## Definition

**Total Dissolved Solids (TDS)** is a measure of the combined content of all inorganic and organic substances contained in a water sample that are present in a dissolved state (smaller than 2 micrometers, typically passing through a 0.45‑µm filter). It is expressed in milligrams per liter (mg/L) or parts per million (ppm). TDS includes minerals, salts, metals, cations, anions, and some organic matter that are fully dissolved in the water. Common constituents include calcium, magnesium, sodium, potassium, chloride, sulfate, bicarbonate, and nitrate.

TDS is a key water quality indicator for drinking water, irrigation, industrial processes, and environmental monitoring. High TDS can affect taste, scaling potential, and aquatic life.

## How it works

TDS is measured using two primary methods: **gravimetric analysis** and **electrical conductivity (EC) measurement**.

### Gravimetric method (laboratory standard)
1. A water sample is filtered through a 0.45‑µm membrane to remove suspended solids.
2. The filtrate is evaporated to dryness in a pre-weighed dish at 180°C (or 105°C depending on the protocol).
3. The residue weight is recorded, and TDS = (weight of residue – tare weight) / sample volume.
   - This yields an accurate mass-based result but is time‑consuming and requires careful quality control.

### Electrical conductivity method (field / screening)
1. A conductivity probe measures the ability of water to conduct an electrical current.
2. Because dissolved ions (e.g., Na⁺, Cl⁻, Ca²⁺, HCO₃⁻) are the primary charge carriers, EC correlates strongly with TDS.
3. A conversion factor (typically 0.5–0.7 for natural waters) is used: TDS (mg/L) ≈ EC (µS/cm) × K.
   - The exact factor depends on the ionic composition of the water.
   - The method is rapid, inexpensive, and suitable for real‑time monitoring, but it provides an estimate rather than a direct mass measurement.

TDS is also sometimes estimated from total filtered residue (non‑filterable residue) or by summing the concentrations of major ions if complete chemical analyses are available.

## Variants

| Variant / Implementation | Description |
|------------------------|-------------|
| **Gravimetric TDS** | The reference laboratory method described above. Yields a true mass per volume measurement. |
| **Conductivity‑based TDS** | Most common field method. Uses a calibrated conductivity meter with a conversion factor. |
| **Ion summation** | TDS computed as the arithmetic sum of individually analyzed ions (e.g., Ca²⁺, Mg²⁺, Na⁺, K⁺, CO₃²⁻, HCO₃⁻, Cl⁻, SO₄²⁻, NO₃⁻). Assumes no missing major constituents. |
| **Filterable residue (Total Dissolved solids or TDS)** | The residue remaining after filtration through a 0.45‑µm filter, dried at 180°C. Some protocols dry at 105°C, which may retain water of hydration. |
| **Total dissolved solids (TDS) vs. total suspended solids (TSS)** | TDS is the dissolved fraction; TSS is the particulate fraction retained on the filter. Together they equal total solids (TS). |

## Trade-offs

- **Accuracy vs. speed**: The gravimetric method is definitive but slow and requires a well‑equipped lab; conductivity meters provide instant results but depend on calibration and the assumed conversion factor.
- **Ion‑specific effects**: Conductivity‑based TDS estimates can be biased if the water has a high proportion of non‑conducting substances (e.g., dissolved organic carbon, silica) or if the ionic composition deviates from the calibration standard.
- **Filter pore size**: The standard 0.45‑µm cutoff is arbitrary. Colloids (0.001–1 µm) may pass and contribute to TDS or be retained, affecting comparability between studies.
- **Temperature dependence**: Conductivity readings are temperature‑dependent; modern meters automatically correct to 25°C.
- **Spatial and temporal variability**: TDS can vary with rainfall, evaporation, geological formations, and anthropogenic inputs (e.g., road salt, agricultural runoff, wastewater). Single grab samples may not represent average conditions.
- **Regulatory limits**: Drinking water standards (e.g., US EPA secondary maximum contaminant level of 500 mg/L) are based on palatability, not health risk, so exceeding the limit is not necessarily harmful but may affect taste.

## See also

- Electrical Conductivity
- Suspended Solids
- Water Quality Parameters
- Salinity
- Hardness
- Ion Chromatography
- Gravimetric Analysis