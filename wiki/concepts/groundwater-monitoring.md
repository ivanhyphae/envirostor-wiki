---
concept: groundwater-monitoring
entity_type: technique
aliases: ["groundwater sampling", "groundwater quality monitoring", "gw monitoring", "groundwater-sampling", "gw-monitoring"]
sources: ["S9525-06-44A Caltrans Modesto Stockpiles GW 0213.pdf", "S9525-01-44B Modesto Stockpiles GW June 2013.0613.pdf", "S9800-01-17 Modesto Stockpiles Feb2014 GW Mon 0414.pdf", "S9525-01-44C Modesto Stockpiles GW September 2013 1013.pdf", "S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf", "raw/DTSC Letter Response - 2025 GW Monitoring Report (900259).pdf", "raw/S9525-06-44A Caltrans Modesto Stockpiles GW Nov2012 0213.pdf", "raw/S1200-01-01 Modesto Stockpiles GW April 2019_06.19.pdf", "raw/S9525-06-44AModesto Stockpiles GW. SEPT2012.1212.pdf", "raw/7453_S9525-06-44_Modesto_Stockpiles_July_2012_GW_Report.1112.pdf", "raw/S2350-01-02 Updated Statistical Evaluation Report_2.24.pdf", "raw/DTSC Letter Response - 2025 GW Monitoring Report (900259) (1).pdf", "raw/S9525-06-44A May 2012 GW Report 1112.pdf", "raw/S9525-06-44AModesto Stockpiles GW SEPT2012 1212.pdf", "raw/S9800-01-17 Modesto Stockpiles Feb2014 GW Mon 0414 (1).pdf", "raw/S9525-06-44 Modesto Stockpiles GW.0612.pdf", "raw/example-gw-monitoring-report.md", "raw/S9525-01-44B Modesto Stockpiles GW June 2013.0613 (1).pdf", "raw/S1200-01-01 Modesto Stockpiles GW April 2017_07.17.pdf", "raw/S9800-01-17 Caltrans Modesto Stockpiles Dec 2013 GW Mon 0114.pdf", "raw/S9800-01-17 Caltrans Modesto Stockpiles GW_06.15.pdf", "raw/S9800-01-17A Caltrans Modesto Stockpiles GW_06 16.pdf", "raw/06A2542ct_TO97_GW Rpt_final.20230308.pdf"]
confidence: high
created_at: 2026-06-04T08:15:23Z
---

# Groundwater Monitoring

## Definition

Groundwater monitoring is the systematic, periodic measurement of groundwater quality and hydraulic conditions at a site. It involves collecting water samples from a network of monitoring wells, analyzing them for physical, chemical, and biological parameters, and measuring water levels to assess groundwater flow direction, contaminant presence, and compliance with regulatory standards.

## How it works

Groundwater monitoring typically follows a standardized workflow:

1. **Network design**: A set of monitoring wells (e.g., MW‑1 through MW‑10) is installed at strategic locations to capture upgradient/downgradient conditions, potential source areas, and background quality. Well construction records (screen depth, casing material, annular seal) are documented.

2. **Field sampling**:
   - **Depth-to-water measurement**: Water level is measured using an interface probe or electronic tape to determine hydraulic head and flow direction.
   - **Well purging**: Three to five casing volumes are removed before sampling to ensure the collected water represents formation groundwater, not stagnant water.
   - **Sample collection**: Samples are obtained using disposable bailers or low‑flow pumps. Field parameters (pH, specific conductance, temperature, dissolved oxygen, turbidity) are recorded.
   - **Preservation and transport**: Samples are placed in appropriate containers, preserved (e.g., HNO₃ for metals, H₂SO₄ for nitrate), and shipped under chain of custody to a laboratory.

3. **Laboratory analysis**:
   - **Dissolved metals**: Analyzed by ICP‑MS (EPA Method 6020) or ICP‑OES; mercury by cold vapor AA (EPA 7470).
   - **Anions (nitrate, chloride, sulfate)**: Determined by ion chromatography (EPA 300.0).
   - **General minerals**: Total dissolved solids (TDS) by SM 2540C; alkalinity, hardness by titration.
   - **Organic compounds**: SVOCs/VOCs by GC/MS if required.

4. **Quality assurance/quality control (QA/QC)**: Field blanks, trip blanks, laboratory control samples (LCS), duplicates, and matrix spikes are processed. Data flags (e.g., “M1” for low matrix spike recovery, “D6” for dilution) indicate limitations.

5. **Data evaluation**:
   - **Comparison to standards**: Dissolved concentrations are compared to Maximum Contaminant Levels (MCLs), Health Advisories (HAs), or site-specific action levels.
   - **Statistical analysis**: Trend tests (e.g., Mann‑Kendall), control charts, or inter‑well comparisons identify changes over time.
   - **Reporting**: Findings are compiled in a groundwater monitoring report, often submitted to regulatory agencies (e.g., DTSC, RWQCB). Reports include tables of analytical results, water level contour maps, and exceedance summaries.

## Variants

- **Sampling frequency**: Some programs require **monthly** or **quarterly** sampling; others use **semiannual** or **annual** events. The Caltrans Modesto Stockpiles reports show bimonthly monitoring.
- **Analyte suite**: Monitoring may target specific **metals** (e.g., barium, lead, arsenic), **inorganic anions** (nitrate, TDS), **organic contaminants** (SVOCs, VOCs), or **general minerals** (calcium, magnesium, iron, manganese).
- **Regulatory context**: Different programs follow **State Water Resources Control Board** or **DTSC** requirements, using MCLs, Notification Levels, or site-specific cleanup goals.
- **Data assessment methodology**: Some programs employ **statistical evaluation** (parametric or nonparametric tests for trend and compliance) while others rely on **simple exceedance tracking**.
- **Well types**: Monitoring can be conducted via **dedicated monitoring wells**, **piezometers** (for water level only), or **multilevel samplers** for vertical profiling.

## Trade-offs

- **Cost vs. coverage**: More wells and higher sampling frequency increase representativeness but raise costs. A sparse network may miss localized contamination.
- **Data quality vs. practicality**: Low-flow sampling reduces turbidity but is slower. Bailers are simpler but may introduce aeration or particulate disturbance. Matrix interference (e.g., high iron, dissolved solids) can require dilution flags (D6), degrading detection limits.
- **Detection limits vs. regulatory standards**: Some analytes (e.g., arsenic, mercury) have very low MCLs; lab reporting limits must be correspondingly low, which increases analytical cost.
- **Temporal resolution**: Infrequent sampling can miss transient events (e.g., storm‑driven infiltration); monthly programs provide better trend detection but may be excessive for stable conditions.
- **Statistical power**: Short monitoring histories (few data points) limit the ability to detect trends. Historical data (as seen in decade‑long Modesto datasets) improves trend analysis.
- **False positives/negatives**: Occasional QA/QC failures (e.g., blank contamination or poor spike recoveries) require careful qualification of results; decisions to resample add time and expense.

## See also

- Groundwater monitoring well
- Water quality standard
- Hydrologic cycle
- Contaminant hydrogeology
- Statistical process control
- Environmental site assessment