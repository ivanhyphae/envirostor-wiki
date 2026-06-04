---
concept: bent-2
entity_type: concept
aliases: ["Bent 2"]
sources: ["Bent 2 Stockpiles Tech Memo.pdf"]
confidence: low
created_at: 2026-06-04T08:21:02Z
---

## Definition
**Bent 2** is a conceptual model or inventory methodology introduced in the *Bent 2 Stockpiles Tech Memo* for categorising and tracking segregated stocks of fissile materials, most commonly plutonium or highly enriched uranium, under the assumption of a fixed isotopic composition and limited inter‑batch mixing. The designation “Bent 2” likely denotes the second iteration of a bending‑curve or batch‑enumeration technique used in nuclear material accountancy for special nuclear materials (SNM).

## How it works
The Bent 2 model partitions a stockpile into discrete “bins” or “tranches” based on isotopic purity and age. Each tranche is treated as a homogeneous mass whose nuclear characteristics (e.g., neutron multiplication, spontaneous fission rate) are approximated by a single representative value. The memo’s technical approach involves:

- **Isotopic segmentation** – Sorting material by weight‑percent of the primary fissile isotope (e.g., <sup>239</sup>Pu or <sup>235</sup>U) and by the concentration of minor isotopes that affect neutron economy.
- **Decay corrections** – Applying time‑dependent decay factors to short‑lived isotopes (e.g., <sup>241</sup>Pu → <sup>241</sup>Am) to recalculate effective mass and heat generation.
- **Aggregation rules** – Defining when two tranches can be combined (e.g., if their isotopic compositions differ by less than a threshold, they are “bent” into a single entry).
- **Reporting thresholds** – Specifying minimum lot sizes below which material need not be reported separately.

The process yields a reduced‑dimensionality inventory that preserves critical safety and safeguards attributes while simplifying the computational burden for stockpile simulation.

## Variants
- **Bent 1** – The predecessor method, which used coarser isotopic bins and did not include decay corrections.
- **Bent 3** (if it exists) – A potential refinement that incorporates burnup‑dependent correlations from reactor discharge records.
- **Continuous‑bend methods** – Alternative approaches that replace discrete bins with continuous smoothing functions, but these require more data and are seldom used in static stockpile assessments.

## Trade-offs
- **Accuracy vs. simplicity** – Bent 2 reduces reporting complexity but introduces small errors when material straddles bin boundaries.
- **Static vs. dynamic** – The model is designed for snapshot inventories; it does not handle real‑time additions or removals well without frequent re‑bending.
- **Isotopic uncertainty** – Relies on declared assay data; unverified mixtures can lead to bin misclassification.
- **Regulatory acceptance** – May not meet the granularity required by international safeguards regimes (e.g., IAEA) for high‑frequency verification.

## See also
- Nuclear material accountancy
- Safeguards by design
- Plutonium isotopic composition
- Stockpile stewardship
- Bent‑rod model *(if related)*