---
concept: standard-penetration-test
entity_type: technique
aliases: ["SPT"]
sources: ["LOTB-N Carpenter OC.pdf"]
confidence: high
created_at: 2026-06-04T08:17:09Z
---

## Definition

The **Standard Penetration Test (SPT)** is an in-situ dynamic penetration test used in geotechnical engineering to determine the relative density and strength of soil, particularly granular soils like sands and silts. It provides a measure of soil resistance to penetration and is widely used for site characterization, foundation design, and liquefaction assessment. The test result is expressed as the **N-value**, which represents the number of blows required to drive a standard split-spoon sampler 300 mm (12 inches) into the soil after an initial seating drive of 150 mm (6 inches).

## How it works

The SPT is performed in a borehole during drilling. The procedure, standardized by ASTM D1586 and similar codes (e.g., BS 1377), involves:

1. **Drilling**: A borehole is advanced to the desired test depth, typically using rotary or auger drilling. The hole is cleaned of disturbed material, and the bottom is leveled.
2. **Sampler assembly**: A standard split-spoon sampler (51 mm outer diameter, 35 mm inner diameter, 610 mm length) is attached to drill rods and lowered to the bottom of the borehole.
3. **Driving**: A 63.5 kg (140 lb) drop hammer is raised and dropped freely from a height of 760 mm (30 inches) onto the drill rods. The hammer fall is guided by a cathead or automated trip mechanism to ensure consistent energy transfer.
4. **Count measurements**: The number of blows is recorded for each 150 mm (6 inches) of penetration. The **N-value** is the sum of blows for the second and third 150 mm increments (i.e., the final 300 mm). The first 150 mm (seating drive) discards disturbed material at the borehole bottom.
5. **Recovery**: The sampler is withdrawn, and the soil sample is retained for visual classification and moisture content testing.

The test is typically repeated at 1.5 m (5 ft) intervals, or at changes in stratum. For cohesive soils, the SPT is less reliable because pore pressure and soil adhesion affect blow counts. Corrections are applied to the raw N-value for factors like:
- **Overburden pressure** (N<sub>60</sub> to normalize to 60% hammer energy efficiency)
- **Hammer energy efficiency** (typically 30–80% of theoretical energy)
- **Borehole diameter**, rod length, and sampler type

## Variants

1. **SPT with energy measurement (SPT-EM)**: Uses instrumented rods to measure actual hammer energy transfer, providing more accurate N<sub>60</sub> values. Common in seismic studies and liquefaction analyses.
2. **Modified SPT (MSPT)**: A lighter or heavier hammer system (e.g., 40 kg or 80 kg) used for very soft or very dense soils, though less standardized.
3. **Auto-SPT**: Fully automated hammers with controlled drop heights and consistent energy delivery, reducing human error.
4. **Tapered cone SPT**: Replaces the split-spoon with a cone tip (e.g., 60° apex angle) for continuous penetration logging, bridging SPT and CPT (Cone Penetration Test) methods.
5. **Seismic SPT**: Records P-wave and S-wave arrival times during penetration for seismic velocity profiling.

## Trade-offs

**Advantages**:
- Widely accepted and standardized globally, providing extensive empirical databases for correlations (e.g., bearing capacity, settlement, liquefaction).
- Simple, robust equipment usable in boreholes with soil sampling.
- Applicable in a wide range of soil types (cohesionless to weakly cohesive).

**Limitations**:
- **Low repeatability**: Blow count variability due to hammer energy differences, operator technique, and borehole bottom disturbance. High scatter in results.
- **Inapplicability in soft clays**: N-values in clays often correlate poorly with undrained shear strength—prefer pressuremeter or triaxial tests.
- **Depth limitation**: Rod friction can affect counts at depths over 30 m, requiring energy correction.
- **Disruptive**: Requires borehole drilling, which disturbs soil and slows field work.
- **Empirical correlations**: N-value to engineering parameters (e.g., relative density, modulus) are site-specific and may not transfer between regions.
- **Safety**: Heavy drop hammer poses risk of injury if mishandled.

**Key trade-off**: SPT is a low-cost, quick field test with extensive historical data but suffers from poor precision and sensitivity compared to CPT or pressuremeter tests. It is often used for preliminary site investigations rather than detailed design.

## See also

- Cone Penetration Test
- Vane Shear Test
- Pressuremeter Test
- Soil Liquefaction
- Geotechnical Site Investigation
- N-value Corrections