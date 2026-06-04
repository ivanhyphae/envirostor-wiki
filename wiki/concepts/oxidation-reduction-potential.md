---
concept: oxidation-reduction-potential
entity_type: concept
aliases: ["ORP", "redox-potential"]
sources: ["raw/S9525-06-44A Caltrans Modesto Stockpiles GW 0213.pdf"]
confidence: high
created_at: 2026-06-04T04:21:15Z
---

## Definition

**Oxidation Reduction Potential** (ORP), also termed **redox potential** or **Eh**, is a quantitative measure of the tendency of a chemical species to acquire electrons (be reduced) or lose electrons (be oxidized) in an aqueous solution. Expressed in millivolts (mV), ORP indicates the overall electron activity of a system. A positive ORP value signifies an oxidizing environment (electron acceptor present), while a negative value denotes a reducing environment (electron donor present).

## How it works

ORP is fundamentally governed by the Nernst equation, which relates the measured potential to the concentrations (or activities) of oxidized and reduced species:

$$E = E^0 + \frac{0.059}{n} \log Q$$

where $E$ is the measured potential, $E^0$ is the standard reduction potential, $n$ is the number of electrons transferred, and $Q$ is the reaction quotient. In practice, ORP is measured using an inert electrode (typically platinum) and a reference electrode (e.g., Ag/AgCl or saturated calomel). The voltage difference between the sensing electrode and the reference electrode is recorded by a high-impedance voltmeter.

Key factors influencing ORP readings include:
- **pH**: The activity of protons affects redox equilibria, especially for reactions involving H⁺.
- **Temperature**: The Nernst equation includes a temperature term; ORP values are usually reported at 25 °C.
- **Dissolved oxygen**: Presence of oxygen strongly contributes to oxidizing conditions.
- **Ionic strength and complexation**: Affect the activity coefficients of electroactive species.

ORP electrodes require periodic calibration using standard redox buffers (e.g., ZoBell's solution or Light's solution) and must be maintained to avoid contamination and drift.

## Variants

While the underlying principle is consistent, ORP measurement systems differ in reference electrode type and reporting convention:

- **Ag/AgCl reference electrode** — Most common in modern field instruments. Potential depends on chloride concentration (typically 3 M KCl or saturated KCl). Readings are often reported *as measured* (relative to Ag/AgCl) or converted to the **standard hydrogen electrode (SHE)** scale by adding the reference electrode potential.
- **Saturated calomel electrode (Hg₂Cl₂)** — Older laboratory standard; less common due to mercury toxicity.
- **Platinum vs. gold sensing electrodes** — Platinum is conventional for general redox measurements; gold may be used where platinum surface poisoning (e.g., by sulfides) is a concern.

Measured ORP values can be expressed relative to different reference scales. The most widely used conversions are:
- ORP(SHE) = ORP(Ag/AgCl) + 199 mV (for 3 M KCl at 25 °C)
- ORP(SHE) = ORP(SCE) + 244 mV (for saturated KCl at 25 °C)

## Trade-offs

- **Calibration drift**: Electrodes are prone to fouling from organic films, sulfide deposits, or platinum surface oxidation, requiring frequent cleaning and recalibration.
- **Mixed potentials**: ORP measures a non‑selective net potential from all redox couples present. The recorded value may not represent any single redox pair, complicating interpretation in complex natural waters.
- **Slow equilibration**: Particularly in poorly poised systems (low concentrations of redox‑active species), ORP readings can drift and require long stabilization times.
- **pH dependence**: Without concurrent pH measurement, ORP data can be ambiguous because many redox reactions involve protons.
- **Temperature sensitivity**: Uncompensated temperature changes cause systematic errors; instruments should include automatic temperature compensation or measurements should be recorded at a controlled temperature.
- **Interferences**: Dissolved gases (e.g., H₂S, NH₃), strong oxidizers (chlorine, ozone), and electrode poisoning can yield inaccurate or erratic readings.

## See also

- Redox reactions
- Nernst equation
- pH
- Dissolved oxygen
- Electrode potential
- Standard hydrogen electrode
- Water quality monitoring