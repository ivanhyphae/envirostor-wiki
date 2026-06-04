---
concept: standard-penetration-test
entity_type: technique
aliases: ["SPT"]
sources: ["raw/LOTB-N Carpenter OC.pdf"]
confidence: medium
created_at: 2026-06-04T03:24:05Z
---

## Standard Penetration Test

### Definition

The **Standard Penetration Test** (SPT) is an in‑situ dynamic penetration test used in geotechnical engineering to determine the resistance of soil to penetration by a standard sampler driven by a hammer of a specific weight dropping from a standard height. The result is expressed as the *N‑value* (blow count), which is the number of hammer blows required to drive the sampler 300 mm (approximately 12 inches) after an initial seating drive of 150 mm. SPT results are widely used for estimating soil strength, relative density, and liquefaction potential, and for correlating with other geotechnical parameters.

### How It Works

The SPT procedure, standardized by ASTM D1586 (and equivalent international codes), follows these steps:

1. **Drilling:** A borehole is advanced to the desired test depth using a drilling method that minimizes disturbance of the underlying soil. Common methods include hollow‑stem augers or rotary drilling with mud.
2. **Sampler insertion:** A split‑barrel sampler (typical outer diameter 51 mm, inner diameter 35 mm) is attached to the end of the drill rod and lowered to the bottom of the borehole.
3. **Seating drive:** The sampler is first driven 150 mm (6 inches) into the soil using a 63.5‑kg (140‑lb) hammer falling freely from a height of 760 mm (30 inches). This seating drive accounts for any disturbed material at the borehole base. The blows for this seating interval are recorded but not used in the N‑value.
4. **Test drive:** The sampler is driven an additional 300 mm (12 inches) in three 75‑mm (3‑inch) increments. The number of blows required for each 75‑mm increment is recorded. The sum of blows for the final two 75‑mm increments (i.e., the last 150 mm) is typically reported as the N‑value, though many standards use the total blows for the full 300 mm. The blows for the first 75‑mm of the test drive are often recorded separately to check for seating effects.
5. **Soil recovery:** After the test, the sampler is retrieved, opened, and the soil sample is recovered for visual classification, moisture content determination, and sometimes laboratory testing.
6. **Energy measurement:** Because hammer energy efficiency varies between rigs and operators, modern practice often involves measuring the actual energy delivered to the rods (E<sub>r</sub>) and correcting the blow counts to a standard energy ratio of 60% (N<sub>60</sub>). Corrections may also be applied for overburden pressure, rod length, borehole diameter, and sampler configuration.

The N‑value (or corrected N<sub>60</sub>) is then used with empirical correlations to estimate soil properties such as:

* Relative density of granular soils
* Undrained shear strength of cohesive soils
* Foundation bearing capacity
* Liquefaction susceptibility
* Soil modulus and settlement parameters.

### Variants

1. **Energy‑corrected SPT (N<sub>60</sub>):** The raw N‑value is adjusted to a reference hammer energy efficiency of 60% using measured or assumed energy transfer ratios. This is the most common variant for modern design.

2. **Overburden‑corrected N‑value (N<sub>1</sub> or (N<sub>1</sub>)<sub>60</sub>):** The N<sub>60</sub> value is further normalized to an effective overburden pressure of 100 kPa (≈1 ton/ft²). This correction is essential for liquefaction assessment and for comparing soil densities at different depths.

3. **Automated SPT (ASTM D6066):** Uses an automatic hammer trip mechanism to improve consistency of drop height and reduce operator variability.

4. **SPT with large (California) sampler:** A larger diameter sampler (76 mm outer, 64 mm inner) is sometimes used in coarse gravelly soils to reduce refusal. The N‑value from this sampler must be corrected using empirical factors.

5. **Hollow‑stem auger SPT:** The test is performed through the open center of the hollow‑stem auger, common in environmental and geotechnical investigations where soil disturbance must be minimized.

6. **Modified SPT for rock:** For very dense or cemented materials, a solid‑cone (rock) tip may replace the standard split barrel, but the test is then more akin to a dynamic probing and correlations are different.

### Trade‑offs and Limitations

* **Operator and equipment variability:** The SPT is highly sensitive to the energy delivered by the hammer, which can vary by ±30‑50% between different rigs and operators. Without energy measurement, N‑values from different sources may not be comparable.
* **Soil disturbance:** The drilling and driving process disturbs the soil, particularly in loose sands and soft clays. The N‑value may not reflect true in‑situ conditions in these materials.
* **Depth limitations:** Rod friction and buckling become significant below about 30 m, limiting reliable application at very great depths.
* **Liquefaction correlation uncertainty:** While SPT is the most common method for liquefaction assessment, the correlations are empirical and heavily based on a limited database of case histories, leading to large uncertainty.
* **Time and cost:** SPT is relatively slow and expensive compared to continuous penetration tests like the Cone Penetration Test (CPT). It provides discrete point data, not continuous profiling.
* **Gravelly soils:** SPT is unreliable in gravels and cobbles because the sampler may become obstructed or broken. Alternative tests (e.g., Becker Hammer Test) are preferred.
* **Low‐energy correction requirement:** Failure to apply energy corrections can lead to underestimation of soil strength and overestimation of bearing capacity, potentially unsafe designs.
* **Environmental concerns:** In contaminated sites, the open borehole may create a pathway for contaminant migration; environmental sampling methods must be integrated.

### See also

* Cone Penetration Test – A continuous, electric‑based alternative to SPT.
* Blow count – General term for the N‑value and its uses.
* Geotechnical investigation – The broader context in which SPT is applied.
* Liquefaction – Assessment using SPT‑based empirical methods.
* Dynamic cone penetration test – A simpler, lighter dynamic test.
* Standard penetration test hammer energy measurement – Detailed procedures for energy calibration.