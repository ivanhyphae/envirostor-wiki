---
concept: composite-sample-count-reduction
aliases: ["composite 3 samples instead of 4", "reduce the number of composite samples"]
sources: ["raw/Borrow Area Sampling Plan Approval E-Mail.pdf"]
confidence: medium
created_at: 2026-04-21T03:09:39Z
---

## Definition

**Composite Sample Count Reduction** is a sampling optimization approach in which multiple individual samples are combined into a smaller number of **composite samples** to reduce the total number of laboratory analyses required. Instead of testing every discrete sample separately, selected samples are pooled according to a predefined plan, allowing the analyst to screen a larger area, batch, or population with fewer tests while preserving enough information to make an approval or disposition decision.

In environmental and materials sampling contexts, composite sample count reduction is often used to lower analytical burden, cost, and turnaround time when a full set of discrete results is not necessary for the decision being made.

## How it works

Composite sample count reduction works by grouping samples that are expected to be similar enough for the intended decision purpose and combining them into a single analyzed sample. The process typically follows these steps:

1. **Define the decision objective**  
   Determine whether the goal is screening, confirmation, compliance demonstration, or characterization. Composite sampling is most suitable when the decision can be based on averaged or representative conditions rather than individual point measurements.

2. **Select grouping logic**  
   Samples are grouped based on criteria such as:
   - geographic proximity
   - depth interval
   - material type
   - time period
   - lot, batch, or area

3. **Prepare the composite**  
   Equal or known proportions of the individual samples are combined into one laboratory sample. The composition method should be documented so the result can be interpreted correctly.

4. **Analyze the composite**  
   The laboratory performs a single analysis on the combined material, reducing the number of analytical runs compared with separate analysis of each constituent sample.

5. **Interpret the result**  
   The composite result is used as a representative value for the grouped samples. Depending on the analyte and protocol, a positive result may trigger follow-up discrete sampling, while a non-detect may be sufficient for screening.

A key technical point is that composite sampling changes the statistical meaning of the result: it usually provides a **group-level average or representative concentration**, not the condition of each original sample.

## Variants

Common variants and related implementations include:

- **Equal-volume compositing**  
  Each constituent sample contributes the same amount to the composite. This is the simplest and most common approach.

- **Weighted compositing**  
  Samples contribute in proportion to area, mass, flow, or another relevant weighting factor. This is used when the composite must represent unequal contributions.

- **Spatial compositing**  
  Samples from adjacent locations are combined to represent a larger area, often used in site characterization or borrow area evaluation.

- **Temporal compositing**  
  Samples collected over time are combined to represent an average condition over a period.

- **Incremental sampling / aggregate sampling**  
  A systematic variant in which many increments are collected and combined to reduce variability and improve representativeness.

- **Two-stage strategy**  
  A composite is used for initial screening, followed by discrete samples if the composite indicates a potential issue.

- **Alternative to full compositing: reduced discrete grid**  
  Instead of combining samples, the sampling design may simply reduce the number of discrete samples collected. This is not the same as compositing, but it is often discussed as a related cost-reduction strategy.

## Trade-offs

Composite sample count reduction offers clear efficiencies, but it introduces important limitations:

- **Lower analytical cost and effort**  
  Fewer lab analyses, lower shipping and handling burden, and faster reporting.

- **Reduced spatial or sample-level resolution**  
  A composite can mask hot spots or outliers that would have been evident in discrete samples.

- **Loss of variance information**  
  Individual sample variability is not directly observed, which can weaken statistical interpretation.

- **Potential dilution of exceedances**  
  A contaminated constituent may be diluted below a detection or action threshold in the composite result.

- **Need for defensible grouping**  
  The method depends on a sound basis for grouping samples; inappropriate grouping can produce misleading results.

- **Method and regulatory acceptance**  
  Some programs or regulators accept compositing only for certain analytes, media, or decision types, and may require confirmatory discrete sampling.

- **Analytical constraints**  
  Some analytes are incompatible with compositing because of instability, cross-contamination risk, volatility, or required preservation conditions.

In practice, the technique is most defensible when used for **screening, characterization, or area-average evaluation** and paired with a plan for follow-up sampling when needed.

## See also

- Composite Sampling
- Discrete Sampling
- Sampling Plan
- Environmental Sampling
- Representative Sampling
- Screening Sampling
- Quality Assurance Project Plan