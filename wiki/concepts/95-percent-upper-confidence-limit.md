---
concept: 95-percent-upper-confidence-limit
entity_type: concept
aliases: ["95% UCL", "95-ucl"]
sources: ["raw/Approval E-mail_Revised Basin 5 Clean Fill Tech Memo.pdf", "raw/Caltrans Modesto Soil Stcokpiles RDIP Variance.pdf", "E-mail Acceptance, Stockpile 1 Wall Footing Sampling Tech Memo.pdf"]
confidence: high
created_at: 2026-06-04T03:25:45Z
---

## 95 Percent Upper Confidence Limit

### Definition

The **95 Percent Upper Confidence Limit** (95% UCL) is a statistical measure used to estimate an upper bound for a population parameter (such as the mean concentration of a contaminant) with 95% confidence. In environmental and regulatory contexts, it is commonly applied to demonstrate that a site or material meets cleanup standards by showing that the true average concentration is likely below a regulatory threshold. The 95% UCL is the value such that, if sampling were repeated many times, the true population mean would be less than or equal to this limit 95% of the time.

### How it works

The 95% UCL is calculated from sample data to account for uncertainty due to limited sample size and variability. The process typically involves:

1. **Data collection**: A set of samples (e.g., soil samples from a stockpile or excavation) is collected and analyzed for target contaminants.
2. **Statistical computation**: The 95% UCL is derived using formulas based on the sample mean, standard deviation, and sample size. For normally distributed data, the standard formula is:
   \[
   UCL_{95} = \bar{x} + t_{0.05, n-1} \times \frac{s}{\sqrt{n}}
   \]
   where:
   - \(\bar{x}\) = sample mean
   - \(t_{0.05, n-1}\) = Student's t-value for 95% confidence with \(n-1\) degrees of freedom
   - \(s\) = sample standard deviation
   - \(n\) = sample size

3. **Comparison to standards**: The calculated 95% UCL is compared against a regulatory threshold (e.g., a maximum contaminant level for clean fill). If the UCL is below the threshold, the material is considered acceptable with a high level of confidence.

For non-normally distributed data, alternative methods like log-transformation, nonparametric bootstrapping, or ProUCL software (recommended by the U.S. EPA) are used to compute the UCL.

In practice, regulatory agencies often require the 95% UCL to be recalculated after removing outliers or using distribution-specific methods. For example, in a technical memorandum for a basin clean fill, the 95% UCL for arsenic was computed as 11.8 mg/kg, which was above the 3.0 mg/kg threshold, indicating the stockpile did not meet criteria for unrestricted use. Conversely, in a Caltrans variance request, samples from soil stockpiles used the 95% UCL to exceed cleanup standards, requiring variance approval.

### Variants

- **Upper Confidence Limit for the Mean (UCLM)**: The most common formulation, estimating the upper bound of the population mean.
- **Upper Prediction Limit (UPL)**: Predicts a future single observation or average from a new sample, used for compliance monitoring.
- **Upper Tolerance Limit (UTL)**: Covers a specified proportion (e.g., 95%) of the population with given confidence, used for risk-based decisions.
- **One-sided vs. Two-sided intervals**: The 95% UCL is a one-sided upper bound, while a 95% confidence interval is two-sided (lower and upper). Regulatory applications often use the one-sided upper limit to focus on exceedance risk.
- **Parametric vs. Nonparametric**: Parametric versions assume a distribution (e.g., normal, lognormal), while nonparametric versions (e.g., bootstrap, Chebyshev) make no distributional assumptions and are used for data with high skewness.
- **ProUCL Software**: The U.S. EPA’s ProUCL tool automates selection of the appropriate UCL method based on data characteristics, offering over a dozen variants tailored to data sets with or without censored values (non-detects).

### Trade-offs

- **Conservative bounds**: The 95% UCL is intentionally conservative (higher than the sample mean) to protect against false negatives (i.e., concluding a site is clean when it is not). This can lead to rejection of materials that are actually safe, increasing remediation costs.
- **Sensitivity to sample size**: Small sample sizes produce wider UCLs due to higher standard error, potentially causing borderline materials to fail. Larger samples yield tighter bounds but increase sampling costs.
- **Distributional assumptions**: Incorrectly assuming normality when data are skewed can yield inaccurate UCLs. For highly skewed data, parametric methods may need log-transformation or nonparametric alternatives, which can be less powerful.
- **Outlier influence**: The UCL is sensitive to outliers, which can inflate the estimate and lead to unnecessary rejection. Regulatory guidance often requires outlier testing and potential removal before computation.
- **Regulatory acceptance**: Not all jurisdictions accept the 95% UCL; some require the maximum detected concentration or other metrics. Compatibility with site-specific cleanup goals must be verified.
- **Interpretation nuance**: The 95% UCL is a statistical inference, not a guarantee. There is a 5% chance that the true mean exceeds the UCL, which may be unacceptable for high-risk contaminants.

### See also

- Confidence Interval
- Hypothesis Testing
- Environmental Compliance Sampling
- ProUCL Software
- Statistical Significance
- Clean Fill Criteria