---
concept: confirmation-sampling
entity_type: technique
aliases: ["post-excavation confirmation sampling"]
sources: ["raw/Stockpile 3 Confirmation Sampling Tech Memo Approval.pdf"]
confidence: medium
created_at: 2026-06-04T08:24:29Z
---

## Confirmation Sampling

### Definition
**Confirmation Sampling** is a statistical quality control technique used to verify that a process or product meets specified requirements by testing a subset of items from a larger population, where the sampling method is designed to confirm (with a predetermined level of confidence) that the population conforms to acceptance criteria, rather than to estimate the population's defect rate. It is often employed in high-stakes environments like nuclear stockpile stewardship, where non-destructive evaluation or material verification is required, and the sampling plan is risk-based to minimize the probability of accepting defective items.

### How it works
Confirmation sampling operates on the principle of hypothesis testing. The process involves:
1. **Defining Acceptance Criteria**: Establish the maximum allowable defect rate (e.g., less than 1% defective) based on application requirements.
2. **Selecting a Sampling Plan**: Choose a sample size and decision rule (number of allowed defective items in the sample) using statistical tables (e.g., from MIL-STD-1916 or ANSI/ASQ Z1.4) or custom calculations. The plan is designed to provide a specified confidence level (e.g., 95%) and power (e.g., 90%) to reject lots with a defect rate at or above the unacceptable level.
3. **Collecting the Sample**: Items are randomly selected from the target population (e.g., a specific production batch or stockpile segment) to ensure representativeness.
4. **Testing the Sample**: Each sampled item undergoes the required inspection or measurement.
5. **Making a Decision**: If the number of defective items in the sample exceeds the allowed count, the entire population is flagged for further investigation (e.g., 100% inspection or rejection). Otherwise, the population is accepted as conforming.

In the context of stockpile confirmation sampling (as referenced in the source), the technique ensures that aging nuclear warhead components meet performance standards without destructive testing. The technical memo approval outlines specific sampling frequencies, test criteria, and decision thresholds derived from reliability models and historical data.

### Variants
Several implementations exist, tailored to different contexts:

- **Attribute Sampling**: Focuses on binary outcomes (defective vs. non-defective) using binomial distribution. Common in manufacturing and stockpile verification.
- **Variables Sampling**: Uses continuous measurements (e.g., dimensions, yield strength) and statistical distributions (e.g., normal) to confirm conformance with tighter tolerances.
- **Sequential Sampling**: Tests items one by one, with a dynamic decision to accept, reject, or continue sampling, reducing average sample size for high-quality populations.
- **Bayesian Confirmation Sampling**: Incorporates prior knowledge (e.g., historical defect rates or process capability) into the sampling plan, updating confidence based on sample results. This is particularly relevant for stockpile stewardship where prior data on aging effects is available.
- **Risk-Based Sampling**: Prioritizes sampling from high-risk subgroups (e.g., older components or those with known processing anomalies) to maximize detection of potential issues.

### Trade-offs
- **Statistical vs. Practical Risk**: Confirmation sampling trades off the risk of accepting defective items (consumer risk) against the risk of rejecting good items (producer risk). Plans with higher confidence levels require larger samples, increasing cost and time.
- **Sample Size Constraints**: In stockpile applications, destructive testing of a single warhead component is extremely expensive and irreversible. Small sample sizes (e.g., n=3–10) are common, but this reduces statistical power, requiring careful calibration of acceptance criteria.
- **Assumption of Homogeneity**: The technique assumes the population is uniform. If the stockpile contains heterogeneous items (due to varying ages or manufacturing processes), random sampling may miss localized defects. Stratified sampling can mitigate this but adds complexity.
- **Limited to Attribute Data**: In some variants, only binary results are used, discarding potentially valuable parametric information (e.g., degradation trends). Variables sampling addresses this but requires more sophisticated analysis.
- **Dependence on Historical Data**: Bayesian variants rely on accurate priors, which may be uncertain for novel aging mechanisms. Overconfidence in prior information can lead to underestimation of actual defect rates.
- **Regulatory and Documentation Overhead**: In regulated environments like nuclear weapons stockpiles, confirmation sampling plans must be formally approved and meticulously documented, as seen in technical memo approval processes.

### See also
- Statistical process control
- Acceptance sampling
- MIL-STD-1916
- Bayesian inference in quality engineering
- Stockpile stewardship
- Risk-based testing
- Non-destructive evaluation