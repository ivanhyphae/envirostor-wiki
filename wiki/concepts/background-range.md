---
concept: background-range
entity_type: concept
aliases: ["site-specific-background"]
sources: ["raw/Caltrans Modesto Soil Stcokpiles RDIP Variance.pdf", "raw/Stockpile 1 MSE Wall Sampling Tech Memo.pdf"]
confidence: low
created_at: 2026-06-04T08:25:41Z
---

## Definition

In environmental site assessment and remediation, **Background Range** refers to the statistical range (typically a lower and upper value) of the concentration of a chemical constituent that is present in soil, sediment, or groundwater due solely to natural geologic processes or diffuse anthropogenic sources (e.g., regional atmospheric deposition) – not from a specific release or contamination event at the site under investigation. It serves as a baseline against which measured concentrations in site media are compared to determine if a release has occurred or if remediation is warranted.

The background range is usually established for inorganic elements (arsenic, lead, chromium, nickel, etc.) and occasionally for naturally occurring organic compounds. It is defined by collecting samples from areas unaffected by the site’s operations and applying statistical methods to derive an upper or interval estimate.

## How it works

1. **Sample collection**  
   Representative background samples are collected from areas that are geologically and geochemically similar to the site but are not influenced by the site’s historical activities. For soil stockpiles (as implied by the source documents), background samples may be taken from undisturbed native soil adjacent to the pile footprint or from regional soil surveys.

2. **Laboratory analysis**  
   Samples are analyzed for the target analytes (metals, pH, organic carbon, etc.). Quality assurance/quality control (QA/QC) procedures are applied to ensure data validity.

3. **Statistical computation**  
   The background range is typically derived using one of the following approaches:
   - **Mean ± 2 standard deviations** (assuming normality, or after log-transformation).
   - **Upper prediction limit (UPL)** – a one-sided interval that covers a specified proportion (e.g., 95%) of future individual measurements.
   - **Upper tolerance limit (UTL)** – a one-sided interval that contains a specified proportion of the population with a given confidence level.
   - **Non-parametric percentiles** – e.g., the 95th or 98th percentile when data cannot be transformed to normality.

   The result is a single upper bound (or in some cases a lower bound) that defines the “background range.” Concentrations above the upper bound are considered elevated (i.e., potentially related to a release).

4. **Comparison with site data**  
   Site soil concentrations from stockpiles or excavation areas are compared to the background range. If a sample exceeds the upper bound, it may trigger further investigation or remediation (depending on regulatory criteria).

## Variants

- **Site-specific background**  
  Derived from samples collected on or immediately adjacent to the site from units that are lithologically equivalent to the impacted media. Preferred when local natural variability is high.

- **Regional background**  
  Based on data from large soil surveys (e.g., USGS, NRCS) covering a broader area. Used when onsite background sampling is not feasible or when the site has been extensively disturbed.

- **Default/generic background**  
  Published regulatory thresholds (e.g., California’s Background Concentrations for Arsenic) that serve as a screening-level background. These are often conservative and may not reflect actual site conditions.

- **Dynamic background (temporal)**  
  For groundwater, background range may shift seasonally or due to regional hydrologic changes; updates may be needed over time.

## Trade-offs

- **Spatial variability**  
  Natural soil composition can vary dramatically over short distances. A small number of background samples may not capture the full range, leading to false positives (calling clean soil contaminated) or false negatives (missing real contamination).

- **Statistical assumptions**  
  Parametric methods require normally distributed data; many soil contaminants follow lognormal distributions. Using the wrong transformation can produce unreliable bounds.

- **Sample size**  
  Reliable background range estimation typically requires at least 8–10 samples per distinct geologic unit. Fewer samples reduce statistical power and widen confidence intervals.

- **Cost vs. rigor**  
  Collecting and analyzing a robust set of background samples adds project cost, but failing to establish an appropriate range may lead to unnecessary remediation or regulatory non-compliance.

- **Comparable laboratory methods**  
  Background and site samples must be analyzed by the same method (e.g., EPA Method 6010B for metals) and similar detection limits to avoid bias.

- **Legacy anthropogenic contributions**  
  In urban or agricultural areas, widespread diffuse contamination (e.g., lead from historic vehicle emissions) may confound natural background. Delineating natural vs. anthropogenic contribution can be difficult.

## See also

- Contaminant of Concern
- Soil Remediation Levels
- Risk-Based Screening Levels
- Geochemical Baseline
- Upper Prediction Limit
- Statistical Tolerance Interval
- Caltrans Environmental Manual

---