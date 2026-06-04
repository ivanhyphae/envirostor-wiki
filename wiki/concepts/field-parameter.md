---
concept: field-parameter
entity_type: concept
aliases: ["field measurements", "water quality parameters"]
sources: ["raw/S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.pdf", "raw/S1200-01-01 Modesto Stockpiles Dec 2016 SW Sampling_01.17.pdf"]
confidence: medium
created_at: 2026-06-04T03:21:46Z
---

## Definition

In environmental monitoring, a **field parameter** is a physical, chemical, or biological property of a water sample that is measured on‑site (in the field) immediately after collection, rather than being transported to a laboratory for analysis. These measurements capture conditions that may change rapidly after sample removal from the source (e.g., due to degassing, temperature shifts, or biological activity). Common field parameters include temperature, pH, specific conductance, dissolved oxygen, turbidity, and oxidation‑reduction potential (ORP).

Field parameters are essential for characterizing water quality at the point of collection, providing context for laboratory analyses, and ensuring that sample handling does not introduce artifacts.

## How it works

Field parameter measurement follows a standardized workflow:

1. **Equipment Preparation** – Sensors (e.g., multiparameter probes, thermometers, turbidimeters) are calibrated before each sampling event using known standards (e.g., pH buffers, conductivity standards). Calibration logs are maintained to ensure traceability.

2. **On‑Site Measurement** – At the sampling point (e.g., a monitoring well or surface water station), the collected water is measured as soon as possible – often in a flow‑through cell or a dedicated sample container. Sensors are rinsed with deionized water or sample water between measurements to avoid cross‑contamination.

3. **Recording** – Values are recorded on a standardized field form or in an electronic data logger, along with metadata such as time, weather conditions, and equipment serial numbers.

4. **Quality Control** – Duplicate or replicate measurements are taken at a frequency specified by the project’s Quality Assurance Project Plan (QAPP). Field blanks (deionized water) and equipment blanks may also be analyzed to verify that sampling equipment has not introduced contamination.

The principle behind field parameter measurement is that certain properties are labile – they will change if the sample is stored or transported. For example, dissolved oxygen can be consumed by microbial respiration, and pH can shift as carbon dioxide degasses. By measuring these parameters in the field, the data represent the true in‑situ conditions at the moment of collection.

## Variants

While field parameters generally refer to physical and chemical measurements, they can be categorized by the type of property:

- **Physical parameters**: temperature, turbidity, total dissolved solids (TDS) via specific conductance.
- **Chemical parameters**: pH, dissolved oxygen (DO), oxidation‑reduction potential (ORP), alkalinity (sometimes measured titrimetrically in the field).
- **Biological parameters**: in limited contexts, field‑portable chlorophyll or **E. coli** tests (e.g., using Colilert®) are considered field parameters, though most biological analyses require laboratory incubation.

Different regulatory programs may define a specific list of required field parameters. For instance, groundwater monitoring at the **Modesto Stockpiles** site (as referenced in the source reports `S9800-01-17` and `S1200-01-01`) likely includes temperature, pH, specific conductance, and turbidity as standard field parameters for both groundwater wells and surface water sampling stations. The reports cover June 2014 (groundwater) and December 2016 (surface water) sampling events, where field parameters were recorded along with laboratory analyses for constituents such as metals, volatile organic compounds, or pesticides.

## Trade-offs

| Advantage | Consideration |
|-----------|---------------|
| Captures unstable conditions | Instruments require careful calibration and maintenance; errors can propagate if calibration drifts. |
| Provides immediate quality screening | Subjective operator technique can introduce variability; not all parameters can be measured in the field (e.g., nutrients, trace metals). |
| Reduces sample transport artifacts | Field measurements add time to the sampling event, increasing field crew costs. |
| Supports real‑time decision‑making | Some field parameters (e.g., DO, turbidity) are only proxies for more precise laboratory analyses. |

Key limitations:
- Sensor accuracy is generally lower than laboratory instrumentation.
- Some parameters (e.g., alkalinity) can be measured in the field but require titration and may be operator‑sensitive.
- Field conditions (extreme temperatures, high turbidity) can interfere with optical sensors.
- Data must be rigorously documented and linked to the corresponding laboratory sample to ensure data usability.

## See also

- Groundwater Sampling
- Surface Water Sampling
- Quality Assurance / Quality Control
- Multiparameter Probe
- Sample Preservation and Handling
- Calibration Standards
- Modesto Stockpiles Site Investigations