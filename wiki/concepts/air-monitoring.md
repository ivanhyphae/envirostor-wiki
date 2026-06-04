---
concept: air-monitoring
entity_type: technique
aliases: []
sources: ["Draft Interim RACR_ App D-G.pdf"]
confidence: low
created_at: 2026-06-04T03:27:25Z
---

## Definition

Air monitoring is the systematic measurement and analysis of airborne contaminants—gases, vapors, particulate matter (PM), or biological agents—to assess their concentration over a specified time and location. It serves to evaluate exposure risks, verify compliance with regulatory limits, and inform public health or industrial hygiene decisions. The Draft Interim RACR App D–G likely defines monitoring protocols within a regulatory framework (e.g., Risk Assessment and Corrective Action for contaminated sites).

## How it works

Air monitoring generally follows a four-stage process: **planning**, **sampling**, **analysis**, and **interpretation**.

1. **Planning**  
   Define objectives (e.g., occupational exposure assessment, ambient air quality). Select target analytes based on site history, emission sources, or regulatory lists. Determine spatial and temporal coverage (fixed stations, personal dosimeters, mobile surveys). Set detection limits and sampling duration (grab vs. continuous).

2. **Sampling**  
   - **Active sampling**: Air is drawn through a collection medium (filter, sorbent tube, impinger) using a calibrated pump. Flow rate and volume are recorded to calculate concentration.  
   - **Passive sampling**: Diffusive samplers (e.g., badges, tubes) rely on molecular diffusion; no pump required, ideal for long-term average concentrations.  
   - **Direct‑reading instruments**: Real‑time sensors (electrochemical, photoionization, light‑scattering) provide instantaneous or rolling average data.

3. **Analysis**  
   - **Gravimetric**: Filters weighed pre‑ and post‑sampling for PM mass.  
   - **Chromatographic**: Gas chromatography (GC) or high‑performance liquid chromatography (HPLC) for volatile organic compounds (VOCs) and semi‑volatiles.  
   - **Spectroscopic**: Fourier‑transform infrared (FTIR), atomic absorption (AA), or inductively coupled plasma (ICP) for metals and specific gases.  
   - **Biological**: Culture, PCR, or enzymatic assays for bioaerosols.

4. **Interpretation**  
   Compare measured concentrations to reference values: permissible exposure limits (PELs), threshold limit values (TLVs), or ambient air quality standards. Account for sampling time, meteorological conditions, and background levels. Uncertainty analysis (e.g., measurement error, breakthrough) is essential.

## Variants

- **Area monitoring**: Stationary samplers placed at fixed locations (e.g., fenceline, work areas). Used for background or perimeter compliance.  
- **Personal monitoring**: Sampler worn by an individual (e.g., lapel badge, portable pump) to measure breathing‑zone exposure.  
- **Continuous monitoring**: Automated instruments (e.g., gas chromatographs, chemiluminescence NOx analyzers) provide real‑time data streams, often with telemetry.  
- **Grab sampling**: Single sample collected over a short period (seconds to minutes) for instantaneous concentration. Suitable for leak detection or process upset events.  
- **Integrated (time‑weighted) sampling**: Sampler runs over 8 hours or longer to yield an average concentration (e.g., for OSHA compliance).  
- **Remote or optical monitoring**: Open‑path FTIR, differential optical absorption spectroscopy (DOAS), or LIDAR measure path‑averaged concentrations across a line or volume.

## Trade-offs

| Consideration | Active / Continuous | Passive | Grab |
|---------------|-------------------|---------|------|
| **Cost**      | Higher (pumps, calibration, power) | Lower (no pump, less maintenance) | Low per sample but many may be needed |
| **Time resolution** | Excellent (real‑time) | Poor (integrated over days–weeks) | Single‑point in time |
| **Detection limits** | Low (active) to excellent (instrument‑specific) | Moderate (depends on diffusion coefficient) | Variable (can be ppb with canisters) |
| **Interferences** | Common (e.g., humidity, co‑contaminants) | Reduced but still subject to sorbent saturation | Mitigated by analytical method |
| **Mobility** | Low‑moderate (bulky equipment) | High (lightweight) | High (canisters, bags) |
| **Data representativeness** | High when continuous; area monitoring may miss spatial hotspots | Average; poor for peak events | Captures only momentary conditions |

Additional trade‑offs: **breakthrough** (active sorbent saturation), **sample stability** (reactive compounds degrade), **meteorological influence** (wind, temperature), and **regulatory acceptance** (passive samplers may not be approved for compliance in some jurisdictions).

## See also

Particulate matter
Volatile organic compounds
Industrial hygiene
Exposure assessment
Air quality index
Draft Interim RACR (regulatory context)