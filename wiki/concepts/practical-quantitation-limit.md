---
concept: practical-quantitation-limit
entity_type: concept
aliases: ["PQL", "practical quantitation limit"]
sources: ["raw/S1200-01-01 Modesto Stockpiles Oct 2016 SW Sampling_12.16.pdf"]
confidence: medium
created_at: 2026-06-04T04:08:28Z
---

## Definition

The **Practical Quantitation Limit** (PQL) is the lowest concentration of an analyte that can be reliably quantified with acceptable accuracy and precision under routine laboratory conditions. It represents a performance-based threshold for reporting quantitative results, distinct from the more stringent Method Detection Limit (MDL). In environmental and regulatory contexts, the PQL is often defined as 5–10 times the MDL, but it may also be set based on statistical criteria from replicate analyses (e.g., relative standard deviation ≤20%) or as the lowest calibration standard that meets predefined quality objectives.

## How it works

The PQL is established by first determining the Method Detection Limit|MDL—the minimum concentration that can be measured and reported with 99% confidence that the analyte is present. The PQL is then typically calculated by multiplying the MDL by a factor (commonly 5 or 10) to ensure that the quantification uncertainty is acceptable for the intended use. Alternatively, laboratories may derive the PQL by analyzing spiked samples at decreasing concentrations and identifying the lowest level at which accuracy (e.g., recovery within 70–130%) and precision (e.g., RSD ≤20%) criteria are consistently met. This empirical approach accounts for matrix effects, instrument performance, and routine operational variability.

In practice, the PQL is the concentration above which the laboratory can confidently report a numeric value without qualifying it as "estimated" or "below the quantitation limit." Results between the MDL and PQL are often reported as "detected but not quantified" or as estimated values.

## Variants

Several related terms are used interchangeably, though subtle distinctions exist:

- **Limit of Quantitation (LOQ)**: Often synonymous with PQL, but LOQ is more rigorously defined in analytical chemistry as the concentration at which the signal-to-noise ratio is at least 10:1. Many regulatory programs use LOQ as the official quantitation limit.
- **Reporting Limit (RL)**: The concentration above which a laboratory will report results without qualification. This is sometimes set equal to the PQL or LOQ, but may be adjusted for sample-specific factors (e.g., dilution, matrix interference).
- **Estimated Quantitation Limit (EQL)**: A term used when the PQL cannot be precisely determined, often due to limited data or complex matrices. It carries greater uncertainty.

## Trade‑offs

- **Sensitivity vs. reliability**: Lowering the PQL increases the chance of detecting trace contaminants, but also raises the risk of false positives or of reporting concentrations with unacceptable imprecision.
- **Regulatory compliance**: Setting a PQL too low may lead to frequent exceedances of action levels; too high may mask contamination that warrants remediation.
- **Laboratory resources**: Achieving lower PQLs often requires more sensitive instrumentation, cleaner backgrounds, or extensive method validation, increasing cost and turnaround time.
- **Data usability**: Regulatory decisions depend on comparability across laboratories. Inconsistent PQL definitions can hinder data interpretation and site-to-site comparisons.

## See also

- Method Detection Limit
- Limit of Detection
- Analytical Quality Control
- Environmental Monitoring
- Calibration Curve