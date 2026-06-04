---
concept: 95-percent-upper-confidence-limit
entity_type: technique
aliases: ["95-ucl"]
sources: ["raw/E-mail Acceptance, Stockpile 1 Wall Footing Sampling Tech Memo.pdf"]
confidence: medium
created_at: 2026-06-04T08:26:43Z
---

## Definition

The **95 percent upper confidence limit** (UCL₉₅) is a one‑sided upper bound of a confidence interval, constructed such that, under repeated sampling, the true population parameter (e.g., mean, median, or percentile) will be less than or equal to this bound in 95% of samples. It is widely used in environmental monitoring, industrial quality control, and risk assessment to provide a conservative estimate of a parameter when the focus is on not underestimating a potential exposure or contamination level.

## How it works

The UCL₉₅ is derived from classical frequentist inference. For a population parameter θ, a one‑sided upper confidence bound is defined as a statistic U such that:

\[
P(\theta \le U) = 0.95
\]

### Common case: mean of a normally distributed population

If the sample mean \(\bar{x}\) and sample standard deviation \(s\) are computed from \(n\) independent observations, and the data are assumed to come from a normal distribution, the UCL₉₅ for the population mean \(\mu\) is:

\[
\text{UCL}_{95} = \bar{x} + t_{0.95, n-1} \cdot \frac{s}{\sqrt{n}}
\]

where \(t_{0.95, n-1}\) is the 95th percentile of Student’s t‑distribution with \(n-1\) degrees of freedom.

For large \(n\) (typically \(n > 30\)) the normal quantile \(z_{0.95} \approx 1.645\) may be used instead.

### Other parameters and distributions

- **Proportion**: For a binomial proportion \(p\), the UCL₉₅ can be computed using the Wilson score interval or the Clopper‑Pearson exact method.
- **Percentiles**: Nonparametric UCL₉₅ for a percentile (e.g., the 95th percentile) can be obtained via order statistics or bootstrapping.
- **Skewed distributions**: When data are log‑normal or heavily skewed, the UCL₉₅ for the mean may be computed using transformed data (e.g., log‑normal UCL) or nonparametric methods such as the Chebyshev inequality or bootstrap‑t intervals.

## Variants

Several implementations and alternatives exist depending on the data characteristics and regulatory guidelines:

| Variant | Description | Common use |
|---------|-------------|------------|
| **Student’s t UCL** | Based on the t‑distribution; assumes normal data. | Standard for small samples. |
| **Normal‑based UCL** | Uses \(z_{0.95}\); acceptable for large samples. | Quick approximation. |
| **Log‑normal UCL** | Applies UCL on log‑transformed data and back‑transforms. | Environmental data often log‑normal. |
| **Nonparametric UCL** | Uses order statistics or bootstrap methods. | No distributional assumption. |
| **Provisional UCL (Helsel)** | Modified method for censored data (e.g., below detection limit). | Water quality and remediation. |
| **One‑sided vs. two‑sided** | One‑sided upper bound vs. two‑sided interval. | UCL₉₅ is one‑sided. |

## Trade‑offs

- **Conservatism**: The UCL₉₅ is intentionally conservative; it may overestimate the true parameter in many samples, leading to more stringent (and costly) decisions in environmental cleanup.
- **Sample size sensitivity**: With small \(n\), the t‑based UCL becomes very wide, reducing its informativeness.
- **Distributional assumptions**: Using the normal‑based UCL on skewed data can drastically underestimate the true upper bound.
- **Misinterpretation**: The UCL₉₅ is **not** the probability that the parameter lies below the bound in a particular sample; that interpretation is Bayesian. Frequentist confidence statements refer to long‑run coverage.
- **Regulatory acceptance**: Many agencies (e.g., US EPA) prescribe specific UCL calculation methods for background versus contaminated sites, and using the wrong variant may invalidate a decision.

## See also

- Confidence interval
- Student's t‑distribution
- Upper prediction limit
- Hypothesis testing
- Chebyshev's inequality
- Log‑normal distribution
- Nonparametric statistics