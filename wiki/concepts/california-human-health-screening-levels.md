---
concept: california-human-health-screening-levels
entity_type: concept
aliases: ["CHHSLs", "chhsls"]
sources: ["7083_S9525-06-44 Modesto Soil Stockpiles Fenceline Workplan.0912 (1).pdf", "raw/S9525-06-44 Modesto Stockpiles SSI Report Rev.0313.pdf"]
confidence: medium
created_at: 2026-06-04T08:19:03Z
---

## Definition

**California Human Health Screening Levels (CHHSLs)** are risk-based concentrations for chemicals in soil, groundwater, and other environmental media developed by the **California Environmental Protection Agency (Cal/EPA)**, primarily for use in evaluating contaminated sites under state cleanup programs. They represent concentrations below which no further action or risk assessment is typically necessary to protect human health. CHHSLs are analogous to the **U.S. EPA Regional Screening Levels (RSLs)** but incorporate California-specific exposure assumptions (e.g., ingestion rates, body weights, exposure durations) and toxicity values.

## How it works

CHHSLs are derived using standard risk assessment equations from the U.S. EPA, combined with California-specific parameters and default exposure scenarios. For carcinogenic effects, the target risk level is generally **1 × 10⁻⁶** (one excess cancer case per million people exposed). For non‑carcinogenic effects, the target hazard index (HI) typically **equals 1** (no adverse effects).

The process involves the following steps:

1. **Selection of toxicity values**: California uses either its own **Cal/EPA toxicity values** (e.g., from the Office of Environmental Health Hazard Assessment, OEHHA) or, where those are unavailable, values from the **U.S. EPA Integrated Risk Information System (IRIS)**.

2. **Definition of exposure pathways**: Standard pathways include:
   - Ingestion of soil, groundwater, or dust.
   - Inhalation of vapors or airborne particulates.
   - Dermal contact with soil or water.
   - Consumption of home‑grown produce or livestock (for agricultural scenarios).

3. **Application of exposure assumptions**: California default values are used for body weight, soil ingestion rate, inhalation rate, exposure frequency, and duration. Examples include a **70‑year lifetime** for cancer risk and a **30‑year averaging time** for non‑cancer hazard; a **15‑kg child body weight** for residential scenarios; and site‑specific exposure frequencies (e.g., 350 days/year for residential, 250 for commercial/industrial).

4. **Calculation**: For each chemical and pathway, the screening level is computed as:

   \[
   \text{CHHSL} = \frac{\text{TR} \times \text{AT}}{\text{SF} \times \text{EF} \times \text{ED} \times \text{IR}}
   \]

   where TR = target risk, AT = averaging time, SF = slope factor, EF = exposure frequency, ED = exposure duration, IR = intake rate. Non‑cancer levels use reference doses (RfDs) or reference concentrations (RfCs).

5. **Comparison with site data**: CHHSLs are used as a screening tool: if a contaminant concentration in soil or water is below the applicable CHHSL, the site is considered to pose an acceptable risk for that pathway. Levels exceeding a CHHSL do not indicate a risk per se but trigger further site‑specific evaluation.

## Variants

CHHSLs are published for different media and land use scenarios:

- **Residential soil CHHSLs** – based on a child receptor (most sensitive).
- **Commercial/industrial soil CHHSLs** – assume adult worker exposure.
- **Construction worker soil CHHSLs** – short‑term exposure for digging and disturbance.
- **Groundwater CHHSLs** – for ingestion and direct‑contact pathways.
- **Vapor intrusion CHHSLs** – derived for groundwater‑to‑indoor‑air inhalation.
- **Tap water CHHSLs** – for drinking water from groundwater.

Alternatives include **U.S. EPA RSLs** (national default values), **Texas Tier 1 Protective Concentration Levels**, and **Alaska’s Soil Cleanup Levels**. California also publishes **screening levels for ecological receptors** and **site‑specific risk‑based targets**.

## Trade-offs

- **Conservative nature**: CHHSLs are designed to be protective of the most sensitive receptor under default worst‑case assumptions. This can lead to overly stringent cleanup goals for many sites, potentially driving unnecessary remediation costs.
- **Media and pathway limitations**: CHHSLs do not account for combined (cumulative) risks across multiple chemicals or pathways unless explicitly combined in a screening evaluation. Site‑specific risk assessments may be more realistic.
- **Receptor variability**: Default child exposure assumptions may not apply to all sites (e.g., industrial areas with no residential use). In such cases, commercial/industrial CHHSLs may be more appropriate but still contain conservative defaults.
- **Toxicity value differences**: Discrepancies between Cal/EPA and U.S. EPA values can lead to different screening levels for the same chemical, causing confusion among users.
- **No cumulative risk**: The screening level for each chemical and pathway assumes no other chemicals are present, but in reality, mixtures can increase overall risk.
- **Regulatory acceptance**: In California, CHHSLs are widely accepted for **preliminary endangerment assessments** and **brownfields evaluation**, but not all regulatory agencies outside California use them.

## See also

- Risk-Based Screening Levels
- Regional Screening Levels (US EPA)
- California Environmental Protection Agency
- Office of Environmental Health Hazard Assessment (OEHHA)
- Site Remediation
- Vapor Intrusion
- Human Health Risk Assessment