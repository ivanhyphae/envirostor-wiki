---
concept: stiff-diagrams
entity_type: technique
aliases: []
sources: ["raw/S9525-06-44AModesto Stockpiles GW SEPT2012 1212.pdf"]
confidence: medium
created_at: 2026-06-04T08:25:09Z
---

## Definition

**Stiff Diagrams** are graphical representations used in geotechnical engineering and materials science to display the consistency limits (Atterberg limits) of fine-grained soils, specifically showing the relationship between water content and the soil's physical state (liquid, plastic, or solid). They are named after their creator, geotechnical engineer H. Stiff, and are typically plot-based charts that illustrate the water content (w) on one axis against the plasticity index (PI) or other derived parameters, often including boundaries for liquid limit (LL), plastic limit (PL), and shrinkage limit (SL). Stiff Diagrams help classify soils according to systems like the Unified Soil Classification System (USCS) or AASHTO, particularly for cohesive soils with significant clay content.

## How it works

A Stiff Diagram is constructed by plotting a soil sample's measured Atterberg limits—liquid limit (LL), plastic limit (PL), and plasticity index (PI = LL - PL)—on a Cartesian graph. The x-axis typically represents a classification metric (e.g., clay fraction percentage or liquid limit value), while the y-axis shows the plasticity index (PI). Key features of the diagram include:

- **Consistency Limit Lines**: Horizontal or diagonal lines demarcate the liquid limit, plastic limit, and shrinkage limit, separating zones for liquid, plastic, semi-solid, and solid states.
- **Classification Zones**: The diagram is sectioned into regions corresponding to soil types (e.g., CL for low-plasticity clay, CH for high-plasticity clay, ML for low-plasticity silt, MH for high-plasticity silt), following USCS or AASHTO boundaries.
- **Data Points**: Individual soil samples are plotted as points based on their LL and PI. Their position relative to the A-line (a diagonal line with equation PI = 0.73(LL - 20)) determines whether the soil is clay (above the A-line) or silt/organic (below the A-line), as per standard classification.

The diagram is generated from laboratory test data obtained via the Casagrande cup method or fall-cone test for liquid limit, rolling thread method for plastic limit, and mercury immersion or air-drying methods for shrinkage limit. The location of a sample on the Stiff Diagram indicates its engineering behavior: for example, soils with high PI and high LL (CH clays) tend to be highly compressible and have low permeability, while low-PI, low-LL soils (ML) are more silty and prone to liquefaction.

## Variants

- **Casagrande Plasticity Chart**: The most common variant, standard in USCS and AASHTO, uses LL on the x-axis and PI on the y-axis, with the A-line and U-line (upper limit) boundaries. Stiff Diagrams are often synonymous with this chart, though Stiff’s original work may have included additional modifications.
- **Shrinkage Limit Diagram**: Stiff Diagrams can incorporate shrinkage limit data by plotting water content versus volume change or linear shrinkage, showing the transition from plastic to solid state.
- **Three-Phase Plot**: A less common variant includes both Atterberg limits and natural water content (wn) to assess liquidity index and consistency index, providing insight into in-situ soil state.
- **Activity Chart**: Adapted for clay mineralogy, plotting plasticity index against clay fraction percentage to classify clay activity (e.g., kaolinite vs. montmorillonite).

## Trade-offs

- **Advantages**:
  - Provides a rapid, visual classification of fine-grained soils using few laboratory tests.
  - Standardized across USCS and AASHTO, facilitating comparison between projects.
  - Directly correlates with engineering properties such as compressibility, shear strength, and permeability.

- **Limitations**:
  - Sensitive to test method variability (e.g., operator skill in rolling thread tests, drying conditions).
  - Assumes soil behavior is dominated by clay content; non-clay components (silt, organic matter) can shift points unpredictably.
  - Does not account for soil mineralogy or pore water chemistry, which affect real-world behavior (e.g., expansive clays).
  - Fails for non-plastic or granular soils (e.g., sands, gravels), which cannot be classified by Atterberg limits alone.

## See also

- Atterberg Limits
- Unified Soil Classification System (USCS)
- AASHTO Soil Classification System
- Plasticity Index
- Liquid Limit
- Plastic Limit
- Shrinkage Limit
- Casagrande Cup
- Soil Compressibility
- Expansive Clay