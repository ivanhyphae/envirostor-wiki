---
concept: discrete-sampling
entity_type: technique
aliases: ["grab sampling"]
sources: ["raw/SR 132 Stockpile 2 BCS Removal Tech Memo.pdf", "raw/E-mail - Stockpiles 1 and 2 MSE Wall Sampling Plan.pdf"]
confidence: high
created_at: 2026-06-04T03:20:08Z
---

## Definition

**Discrete Sampling** is a data collection methodology where individual, spatially distinct samples are collected from specific locations within a material stockpile or environmental medium, rather than compositing multiple increments into a single sample. Each discrete sample is analyzed separately to preserve spatial variability and detect localized contamination hotspots.

In the context of construction and demolition debris stockpile management, discrete sampling involves extracting single samples from predetermined grid points or depth intervals, allowing for independent characterization of each location's contamination status.

## How it works

The discrete sampling process follows these sequential steps:

1. **Sampling grid design**: A systematic grid is established over the stockpile surface, typically using a regular pattern (e.g., 50–ft grid spacing) with sample locations marked at grid intersections.

2. **Sample collection**: Individual samples of approximately equal mass (often 1–2 kg) are collected from each designated location. In some applications, both surface and depth samples are taken at each grid point to assess vertical heterogeneity.

3. **Independent analysis**: Each discrete sample is separately submitted for laboratory analysis. Samples are never physically combined.

4. **Spatial mapping**: Analytical results are mapped back to their original grid coordinates, creating a spatial contamination profile of the stockpile.

For Material Stockpile Characterization, discrete sampling can be combined with Statistical Sampling to ensure adequate coverage while maintaining spatial resolution.

## Variants

### Grid-based discrete sampling
The most common variant, where samples are collected at regular intervals across the stockpile surface. Grid spacing is determined based on required confidence levels and anticipated contamination heterogeneity.

### Depth-interval discrete sampling
Samples are collected at multiple depth horizons at each grid point (e.g., 0–3 ft, 3–6 ft, 6–10 ft). This variant is particularly useful for stockpiles with vertical stratification of contaminants.

### Random discrete sampling
Sample locations selected via random number generation rather than systematic grid. While less spatially uniform, this approach provides better statistical representation of mean stockpile characteristics.

### Judgment-based discrete sampling
Locations selected based on field observations of staining, odor, or other indicators. This variant may bias results toward contamination hotspots but is resource-efficient.

## Trade-offs

### Advantages
- **Preserves spatial variability**: Detect contamination hotspots that would be diluted in Composite Sampling approaches
- **Enables targeted removal**: Specific areas exceeding cleanup thresholds can be excavated separately
- **Supports geostatistical analysis**: Data can be used for kriging and other spatial interpolation methods
- **Clear accountability**: Each sample result can be attributed to a specific stockpile location

### Disadvantages
- **Higher analytical costs**: Each sample requires separate laboratory analysis, often 3–10 times more expensive than compositing
- **Increased laboratory turnaround**: More samples to process, especially for large stockpiles
- **Potential for misinterpretation**: Single samples may not represent the surrounding volume if stockpile material is highly heterogeneous on small scales
- **Sample handling burden**: More sample containers, labels, and chain-of-custody documentation required

### Comparison with Composite Sampling

| Aspect | Discrete Sampling | Composite Sampling |
|--------|-------------------|-------------------|
| Cost per stockpile | Higher | Lower |
| Hotspot detection | Excellent | Poor |
| Statistical power | Higher per sample | Lower per sample |
| Implementation complexity | More complex | Simpler |
| Data use cases | Spatial mapping, precision removal | Mean characterization only |

## See also

MSE Wall Soil Sampling
Contaminated Soil Management
Statistical Sampling Methods
Geochemical Characterization
Stockpile Volume Estimation