---
concept: mann-kendall-trend-test
entity_type: technique
aliases: ["Mann-Kendall test", "MK test"]
sources: ["S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf"]
confidence: high
created_at: 2026-06-04T08:16:58Z
---

## Definition

The **Mann–Kendall trend test** is a non‑parametric statistical test used to detect the presence of a monotonic (upward or downward) trend in a time series. It does not assume a specific distribution for the data and is robust to outliers. The test evaluates whether the observed values tend to increase or decrease consistently over time, without requiring the trend to be linear.

## How it works

The Mann–Kendall test is based on the Kendall rank correlation coefficient (τ) between the time series values and their chronological order. The test statistic **S** is calculated as:

\[
S = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \operatorname{sgn}(x_j - x_i)
\]

where \(x_i, x_j\) are the data values at times \(i\) and \(j\) (with \(i<j\)), and \(\operatorname{sgn}\) is the sign function (−1, 0, or +1). A positive **S** indicates an increasing trend; negative **S** indicates a decreasing trend.

Under the null hypothesis of no trend and for \(n \ge 8\), **S** is approximately normally distributed with mean zero and variance:

\[
\operatorname{Var}(S) = \frac{n(n-1)(2n+5) - \sum_{k=1}^{m} t_k(t_k-1)(2t_k+5)}{18}
\]

where \(m\) is the number of groups of tied observations and \(t_k\) is the number of ties in the \(k\)-th group. The variance formula corrects for ties.

The standard normal test statistic **Z** is then computed:

\[
Z = 
\begin{cases}
\frac{S-1}{\sqrt{\operatorname{Var}(S)}} & \text{if } S > 0 \\
0 & \text{if } S = 0 \\
\frac{S+1}{\sqrt{\operatorname{Var}(S)}} & \text{if } S < 0
\end{cases}
\]

A two‑sided p‑value is obtained from the standard normal distribution. A small p‑value (e.g., < 0.05) leads to rejection of the null hypothesis, indicating a statistically significant monotonic trend.

The magnitude of the trend is often quantified separately using the **Theil–Sen slope estimator** (the median of all pairwise slopes), which is complementary to the Mann–Kendall test.

## Variants

- **Seasonal Mann–Kendall test** – Designed for data with seasonal cycles. The test is applied separately to each season (e.g., month, quarter), and the individual S statistics are summed to obtain an overall trend, with adjusted variance accounting for seasonal dependence.

- **Mann–Kendall test with serial correlation correction** – Autocorrelation in the time series can inflate the variance of S. Two common corrections are:
  - **Prewhitening**: remove autoregressive components from the data before applying the test.
  - **Variance correction**: adjust the variance of S using an effective sample size based on the autocorrelation coefficient.

- **Modified Mann–Kendall test (e.g., Hamed & Rao, 1998)** – Uses a corrected variance formula that accounts for significant autocorrelation at multiple lags, without prewhitening.

- **Block bootstrap Mann–Kendall** – Resamples blocks of data (to preserve serial dependence) to obtain a bootstrap distribution for S, providing a more robust p‑value.

## Trade-offs

- **Assumption of independence** – The standard test assumes observations are independent. Positive serial correlation increases the false‑positive rate. Prewhitening or variance correction is necessary when autocorrelation is present.
- **Only detects monotonic trends** – The test has low power against non‑monotonic patterns (e.g., cyclic, U‑shaped). It is not suitable for detecting abrupt step changes or multiple turning points.
- **No magnitude estimation** – The test only indicates direction and significance of trend, not its slope. The Theil–Sen estimator is typically used in conjunction.
- **Power with small samples** – For very short time series (n < 8), the test cannot be applied because the normal approximation fails; exact tables are then required, and power is limited.
- **Handling of missing data** – The test is usually applied only to complete records; large gaps may require imputation or case‑wise deletion, which can bias results.
- **Multiple testing** – When applied to many variables (e.g., many monitoring wells), the probability of false positives increases unless corrections like Bonferroni are applied.

## See also

- Kendall rank correlation coefficient
- Theil–Sen estimator
- Time series analysis
- Trend estimation
- Sen's slope
- Autocorrelation correction
- Seasonal Mann–Kendall test