---
concept: icp-ms
entity_type: technique
aliases: ["inductively coupled plasma mass spectrometry"]
sources: ["raw/S9525-06-44A May 2012 GW Report 1112.pdf", "raw/S9800-01-17 Modesto Stockpiles Feb2014 GW Mon 0414 (1).pdf"]
confidence: high
created_at: 2026-06-04T08:24:54Z
---

## Definition

**ICP‑MS** (Inductively Coupled Plasma Mass Spectrometry) is an inorganic analytical technique used for the quantification and isotopic analysis of elements. It combines an inductively coupled plasma (ICP) to atomize and ionize a sample, and a mass spectrometer to separate and detect ions by their mass‑to‑charge ratio (m/z). The technique is known for extremely low detection limits (sub‑parts‑per‑trillion for many elements), broad element coverage (from lithium to uranium), and multi‑isotope capability.

The provided source documents (groundwater monitoring reports) likely rely on ICP‑MS for trace‑metal analysis, but the PDF content is encrypted and could not be parsed; the following information is based on established principles of the technique.

## How it works

1. **Sample introduction** – A liquid sample (typically a dilute acid digest) is pumped via a peristaltic pump into a nebulizer, which creates a fine aerosol. The aerosol passes through a spray chamber, where larger droplets are removed, and is then carried into the ICP torch by a flow of argon gas.

2. **Ionization in the ICP** – The ICP is formed by a radio‑frequency (RF) coil generating an oscillating magnetic field that transfers energy to a flow of argon, producing a high‑temperature plasma (~6000–10,000 K). In the plasma, the sample aerosol is desolvated, atomized, and the atoms are ionized (mostly to singly charged positive ions, M⁺).

3. **Ion extraction and focusing** – Ions from the plasma are sampled through two cones (sampler and skimmer) that separate the atmospheric‑pressure plasma from the high‑vacuum mass spectrometer. Ion lenses electrostatically focus the ion beam into the mass analyzer.

4. **Mass separation** – The most common analyzer is a quadrupole mass filter, which uses oscillating electric fields to selectively transmit ions of a specific m/z. Alternative mass analyzers include sector‑field (for high resolution) and time‑of‑flight (for fast, simultaneous acquisition).

5. **Detection** – Ions that pass through the analyzer strike an electron multiplier (or a Faraday cup for high ion currents). The resulting electrical signal is amplified and recorded. For very low concentrations, the detector operates in pulse‑counting mode; for higher signals, analog mode is used.

6. **Data processing** – Signal intensities are converted to concentrations using calibration standards (external calibration, standard addition, or isotope‑dilution methods). Internal standards (e.g., indium, rhodium) are routinely added to correct for drift and matrix effects.

## Variants

- **Quadrupole ICP‑MS (Q‑ICP‑MS)** – Most common, cost‑effective, with moderate mass resolution (~0.7 amu).
- **High‑resolution ICP‑MS (HR‑ICP‑MS)** – Uses sector‑field mass analyzer; resolves many polyatomic interferences and offers lower detection limits.
- **ICP‑triple quadrupole (ICP‑MS/MS)** – Two quadrupoles with a collision/reaction cell in between; provides advanced interference removal for demanding applications (e.g., geological, semiconductor).
- **ICP‑time‑of‑flight (ICP‑TOF‑MS)** – Simultaneous detection of the entire mass spectrum, suitable for transient signals (e.g., single‑particle/ single‑cell analysis).
- **Laser ablation ICP‑MS (LA‑ICP‑MS)** – Uses a focused laser beam to ablate solid samples directly, eliminating wet digestion.
- **Single‑particle ICP‑MS (spICP‑MS)** – Fast data acquisition to detect and characterize individual nanoparticles.
- **Collision/reaction cell (CRC) variants** – Introduce a gas (e.g., He, H₂, NH₃) to selectively remove polyatomic interferences (e.g., [40Ar¹⁶O]⁺ on [56Fe]⁺).

## Trade‑offs

- **Sensitivity vs. interferences** – ICP‑MS is extremely sensitive but prone to spectral interferences: isobaric (same nominal mass: e.g., ⁹⁹Ru on ⁹⁹Tc), polyatomic (e.g., ⁴⁰Ar³⁵Cl⁺ on ⁷⁵As⁺), and doubly charged ions. Collision/reaction cells mitigate many but not all of these.
- **Matrix effects** – Viscosity, dissolved solids, and concomitant elements can suppress or enhance the analyte signal. Dilution or matrix‑matching is often required.
- **Sample preparation** – Most solid samples must be digested (acid dissolution, microwave‑assisted) to form a liquid suitable for introduction. This adds time and potential contamination.
- **Cost and maintenance** – High argon consumption, consumable cones and torch, expensive RF generator, and skilled operator requirements raise operational costs.
- **Mass range** – Typical quadrupoles are limited to m/z 260; heavier elements (e.g., U) are measurable, but transuranic isotopes may require sector‑field systems.
- **Isotope ratio precision** – While ICP‑MS can measure isotope ratios, precision (0.1–0.5 % RSD) is inferior to thermal ionization mass spectrometry (TIMS) or multicollector ICP‑MS (MC‑ICP‑MS).
- **Signal drift** – Gradual change in sensitivity over time due to cone deposits, plasma fluctuations, or detector aging. Internal standards and frequent recalibration are necessary.

## See also

- Mass Spectrometry
- Inductively Coupled Plasma Atomic Emission Spectroscopy
- Quadrupole Mass Analyzer
- Laser Ablation Inductively Coupled Plasma Mass Spectrometry
- Collision/Reaction Cell
- Trace Element Analysis
- Isotope Ratio Mass Spectrometry
- Multicollector ICP-MS