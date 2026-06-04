---
concept: field-filtered-sample
entity_type: technique
aliases: ["field-filtered", "field filtration sample"]
sources: ["raw/S1200-01-01 Modesto Stockpiles Oct 2016 SW Sampling_12.16.pdf", "raw/S1200-01-01 Modesto Stockpiles Mar 2017 SW Sampling_06.17.pdf"]
confidence: medium
created_at: 2026-06-04T04:07:26Z
---

## Definition

A **Field Filtered Sample** is a water or aqueous‑phase sample that is filtered through a specified filter pore size (typically 0.45 µm) at the sampling site, immediately after collection, prior to preservation and transport to the laboratory. The process removes suspended solids and particulate‑bound analytes, leaving only the dissolved fraction for analysis. Field‑filtered samples are primarily used to characterize dissolved metals, nutrients, or other constituents that are operationally defined as “dissolved” by passing through a 0.45‑µm membrane.

Field‑filtered sampling is a standard technique in environmental monitoring, especially for stormwater runoff, surface water, groundwater, and industrial discharge compliance. The filtration is performed on‑site to avoid changes in analyte partitioning that may occur during storage and transport (e.g., precipitation, adsorption onto container walls, or biological alteration).

## How It Works

1. **Sample Collection** – A representative water sample is collected using an appropriate method (e.g., grab sample, composite sampler) into a clean container.

2. **Field Filtration** – Immediately after collection, the sample is passed through a filter assembly. Common equipment includes:
   - **Syringe‑driven filters** (e.g., 60‑mL syringe with a 0.45‑µm membrane cartridge) for small volumes.
   - **Vacuum or peristaltic pump filtration** for larger volumes, using a filter holder and a pre‑cleaned membrane.
   - **In‑line filters** integrated into sampling equipment (e.g., ISCO autosamplers) for automated filtration.

3. **Preservation and Storage** – Once filtered, the sample is preserved according to the analyte of interest (e.g., acidification to pH < 2 for metals) and stored at 4 °C until laboratory analysis.

4. **Laboratory Analysis** – The laboratory reports dissolved concentrations based on the field‑filtered aliquot. A corresponding total‑recoverable sample (unfiltered) is often collected in parallel to evaluate the particulate‑bound fraction.

### Key Considerations

- **Filter Preparation** – Filters must be pre‑rinsed with deionized water to remove any leachable contaminants. For trace‑metal analysis, acid‑washed filters are recommended.
- **Blanks** – Field blanks (deionized water passed through the filtration system) are essential to verify that no contamination is introduced by the filter or apparatus.
- **Time Constraint** – Filtration must occur within minutes of collection to minimize losses due to adsorption or chemical changes. Standard protocols require filtration within 15 minutes.

## Variants

| Variant | Description |
|---------|-------------|
| **0.45‑µm Membrane Filtration** | The most common definition of “dissolved” for regulatory purposes (e.g., EPA methods). Uses cellulose acetate, cellulose nitrate, or polyethersulfone membranes. |
| **0.2‑µm Filtration** | Used for sterilisation or when a stricter operational definition of “dissolved” is desired (e.g., microbiological studies). |
| **Cross‑Flow Filtration** | Used for high‑turbidity samples to avoid filter clogging; the sample flows tangentially across the membrane, reducing cake formation. |
| **In‑Line Field Filtration** | Filtration is integrated into the sample collection line (e.g., autosampler). Suitable for time‑weighted composite samples. |
| **Field‑Filtered vs. Laboratory‑Filtered** | Laboratory filtration is performed after transport and storage, which may alter speciation. Field filtration minimises such changes. |

## Trade‑Offs and Limitations

- **Operational Definition** – The 0.45‑µm cutoff is an operational, not truly “dissolved,” definition. Colloids smaller than 0.45 µm may pass through and be incorrectly classified as dissolved.
- **Sample Integrity** – Filtration itself can disturb chemical equilibrium (e.g., loss of volatile compounds, oxidation of reduced species, or sorption onto the filter membrane). For metals, acidification after filtration can redissolve some adsorbed species.
- **Clogging and Throughput** – High‑turbidity samples can clog filters rapidly, requiring frequent changes and potentially altering the filtered volume or composition.
- **Cost and Logistics** – Field‑filtration equipment, consumables (filters, syringes, acid), and training add to project costs. The need for immediate filtration restricts the number of sampling locations that can be visited per day.
- **Quality Control** – Field blanks and replicate samples are required to demonstrate that filtration does not bias results. A single contaminated filter batch can invalidate an entire sampling round.

## See Also

- Dissolved Metals
- Total Recoverable Metals
- Stormwater Sampling
- Field Blank
- Operational Definition
- Filter Pore Size