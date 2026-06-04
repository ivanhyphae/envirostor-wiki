---
concept: verification-sampling
entity_type: technique
aliases: ["confirmation sampling", "verification testing"]
sources: ["raw/Acceptance Letter Draft Interim RACR (900259).pdf", "raw/example-racr.md", "raw/SR 132 Stockpile 3 BCS Removal Tech Memo.pdf"]
confidence: high
created_at: 2026-06-04T08:21:29Z
---

## Definition

**Verification sampling** is the systematic collection and analysis of environmental media (e.g., soil, groundwater, air) after a remedial action has been completed to confirm that established cleanup goals, regulatory thresholds, or performance standards have been met. The process provides a statistically defensible basis for demonstrating that residual contamination falls within acceptable limits and that further action is not required. In the context of contaminated site remediation, verification sampling is the final quality assurance step before site closure or transition to long-term management.

## How it works

Verification sampling follows a structured protocol that integrates sampling design, analytical testing, statistical evaluation, and comparison against predefined threshold values. The key steps are:

1. **Establishment of verification thresholds**: Before sampling begins, specific target concentrations (e.g., barium ≤ 1,000 mg/kg for groundwater protection, lead ≤ 80 mg/kg for residential screening) are defined based on risk assessments or regulatory standards (see Risk-Based Screening Levels).

2. **Sampling design**: A sampling plan is developed to ensure that the media of concern are adequately characterized. For soil verification, this often involves systematic grid sampling, judgmental sampling at former hotspots, or composite sampling. The density of samples is tailored to the scale of the remedial area and the variability of contamination.

3. **Sample collection and analysis**: Samples are collected using standard techniques (e.g., hand auger, direct-push, or test pits) and analyzed by an accredited laboratory for the contaminants of interest (e.g., barium, lead). Quality control measures include field duplicates, blanks, and matrix spikes.

4. **Statistical evaluation**: The data are evaluated using tools such as **ProUCL** to calculate upper confidence limits (UCL) of the mean, typically at the 95% confidence level. Nonparametric methods may be preferred when the distribution is skewed (e.g., H-statistic instability). The UCL is compared to the verification threshold.

5. **Decision-making**: If the UCL (or individual sample results, depending on the criterion) falls below the threshold, the area is deemed verified. Areas exceeding thresholds may trigger additional excavation or re‑sampling, as seen in the re‑excavation of hotspots for barium and lead in the referenced project (source: *example-racr.md*).

6. **Documentation**: Results are compiled in a verification report (e.g., an Interim Remedial Action Completion Report) that provides the evidence for compliance and supports regulatory acceptance (see Remedial Action Completion Report).

## Variants

- **Confirmatory sampling**: A subset of verification sampling often used after excavation to test that removal has been complete. It may be more targeted, focusing on sidewalls and bottoms of excavations.
- **Performance‑based verification**: The sampling plan is designed to demonstrate that a specific performance standard (e.g., a maximum contaminant level in groundwater) is achieved, rather than a fixed cleanup goal.
- **Statistical verification**: Relies entirely on statistical inference (e.g., 95% UCL) to confirm that the mean concentration is below a threshold. This approach is common when contamination is heterogeneous.
- **Unit‑specific vs. area‑wide verification**: Sampling may be conducted per discrete remedial unit (e.g., each stockpile) or averaged across a larger consolidated zone, depending on the conceptual site model and regulatory requirements.

## Trade-offs

- **Representativeness vs. cost**: Increasing the number of samples improves statistical confidence but raises analytical and labor costs. Optimal sample numbers must balance the need for defensibility with budget constraints.
- **Threshold selection**: Choosing a single threshold (e.g., a concentration limit) may not account for spatial variability or background levels. If the threshold is set too low, unnecessary re‑excavation may occur; if set too high, residual risk may remain.
- **Temporal considerations**: Verification sampling is a snapshot in time. For contaminants that migrate or degrade, one‑time sampling may not capture long‑term conditions. Post‑closure monitoring may be required (see Long‑Term Monitoring Plan).
- **Statistical method sensitivity**: Nonparametric methods (e.g., bootstrap) are robust to skewed data but may yield a higher UCL than parametric methods, potentially leading to more conservative decisions. The choice of method can significantly affect outcomes.
- **Regulatory acceptance**: Different jurisdictions may accept different levels of statistical rigor. ProUCL calculations may be required by some agencies, while others accept simple comparison of all individual results to thresholds.

## See also

- Confirmatory Sampling
- Remedial Action Completion Report
- Risk-Based Screening Levels
- 95% Upper Confidence Limit
- ProUCL
- Site Closure Criteria