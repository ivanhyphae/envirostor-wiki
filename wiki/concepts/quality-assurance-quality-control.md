---
concept: quality-assurance-quality-control
entity_type: technique
aliases: ["qa/qc"]
sources: ["raw/example-gw-monitoring-report.md", "raw/S9525-01-44B Modesto Stockpiles GW June 2013.0613 (1).pdf", "raw/7084_S9525-06-44 Response to DTSC Workplan Comments.0912.pdf"]
confidence: medium
created_at: 2026-06-04T08:26:10Z
---

## Definition

Quality Assurance / Quality Control (QA/QC) is a systematic framework that combines planned activities (quality assurance) and operational techniques (quality control) to ensure that data, products, or processes meet defined quality standards. In environmental monitoring, QA/QC is essential for generating defensible, reproducible results that support regulatory compliance and decision‑making. QA focuses on preventing defects through process design, training, and documentation; QC focuses on detecting defects through measurements, checks, and corrective actions.

## How it works

QA/QC operates at two levels:

- **Quality Assurance (QA):** Establishes the overall system for quality. This includes developing standard operating procedures (SOPs), training personnel, maintaining equipment, and performing audits. In groundwater monitoring, QA plans specify sampling protocols, analytical methods (e.g., EPA 6020 for dissolved metals, EPA 7470 for mercury, EPA 300.0 for anions), and data validation criteria.

- **Quality Control (QC):** Implements checks to verify that the QA system is functioning. Common QC elements in environmental analyses:
  - **Blanks** (field, trip, method, equipment rinsate) – detect contamination introduced during sampling or analysis.
  - **Laboratory Control Samples (LCS)** – analyte‑free matrix spiked with known concentrations to assess accuracy.
  - **Duplicates** (field or laboratory) – evaluate precision.
  - **Matrix Spikes (MS)** – addition of known amounts of target analytes to a sample to measure matrix effects.
  - **Surrogates** – compounds added to all samples to monitor extraction and analysis efficiency.

Results outside established control limits trigger data flags (e.g., M1, M2, M3 in the example monitoring report) that indicate potential data quality limitations. Dilution factors (D6 flag) may be applied when matrix interference exceeds acceptable ranges.

The process is iterative: QC findings feed back into QA to improve procedures. For example, if matrix spike recoveries consistently fall outside limits, the QA plan may require sample dilution or alternative digestion methods.

## Variants

QA/QC is implemented differently across industries, but the core principles are universal. Common variants include:

- **Laboratory QA/QC:** Internal (calibration standards, blanks, LCS, duplicates, MS) and external (proficiency testing, inter‑laboratory comparisons). Adherence to methods such as USEPA SW‑846 or ISO 17025 is typical.

- **Field QA/QC:** Introduced at the sampling stage. Includes field blanks, trip blanks, replicate samples, and documentation of field conditions. Chain‑of‑custody forms are a QA tool to track sample identity.

- **Programmatic QA/QC:** At the project level, QA is documented in a Quality Assurance Project Plan (QAPP) that outlines objectives, roles, data quality indicators (precision, accuracy, representativeness, completeness, comparability), and corrective action procedures.

- **Industry‑specific standards:**
  - *ISO 9001* – general quality management.
  - *ISO/IEC 17025* – laboratory competence.
  - *EPA QAPP* – mandatory for federally funded environmental projects.
  - *Good Laboratory Practice (GLP)* – pharmaceutical and chemical testing.

- **Adaptive QA/QC:** In iterative projects (e.g., remediation monitoring), QA/QC data are reviewed in near‑real time to adjust sampling frequency, analyte lists, or detection limits.

## Trade-offs

Key considerations when designing and applying QA/QC:

- **Cost vs. Data Quality:** Comprehensive QC (e.g., high frequency of spikes, blanks, and duplicates) increases project cost and turnaround time. Overly stringent QA may delay decision‑making. Underinvestment risks unusable data.

- **Matrix Effects:** Complex samples (e.g., high solids, unusual chemistry) can produce out‑of‑spec QC results, requiring re‑analysis or dilution. The source report notes matrix interference causing “D6” flags and flagged matrix spike recoveries.

- **Confidence vs. Practicality:** Statistical control limits for QC samples balance false‑positive (flagging acceptable data) and false‑negative (accepting poor data) errors. Too narrow limits inflate rejection rates; too wide limits mask true quality issues.

- **Relevance of QC to Project Objectives:** Generic QC may not capture site‑specific challenges. For example, if the primary contaminants are volatile, extra field blanks and trip blanks are warranted, but additional matrix spikes may add little value.

- **Human Factors:** Despite rigorous QA/QC, errors in documentation, sample handling, and data transcription can still occur. Audits and independent reviews are additional safeguards but require time and expertise.

## See also

- Data Quality Objectives
- Environmental Monitoring
- Chain of Custody
- Method Detection Limit
- Quality Assurance Project Plan
- Corrective Action