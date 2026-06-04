---
concept: potentiometric-contour
entity_type: concept
aliases: ["potentiometric surface", "water table contour"]
sources: ["raw/S9800-01-17 Modesto Stockpiles Feb2014 GW Mon 0414.pdf"]
confidence: high
created_at: 2026-06-04T04:07:57Z
---

## Definition

A **potentiometric contour** is a line on a map connecting points of equal hydraulic head (potentiometric surface elevation) in a confined or unconfined aquifer. These contours depict the elevation to which groundwater would rise in a tightly cased well, and are the groundwater analog of topographic contour lines. They are fundamental tools in hydrogeology for visualizing groundwater flow direction, hydraulic gradients, and aquifer recharge/discharge zones.

## How it works

1. **Data Collection**: Water levels are measured in a network of monitoring wells at a consistent time (synoptic survey). Elevations are surveyed relative to a common datum (e.g., mean sea level) to compute hydraulic head values.

2. **Interpolation**: Measured head points are used to generate a continuous surface via interpolation methods such as kriging, inverse distance weighting, or spline. The interpolation assumes the potentiometric surface is a smooth, continuous function of space.

3. **Contouring**: Interpolated values are then contoured (e.g., using software like Surfer, ArcGIS, or manually) to produce lines of equal head. Contour intervals are chosen based on the range of heads and desired detail—common intervals are 1, 5, or 10 feet (or meters).

4. **Interpretation**: Groundwater flows perpendicular to potentiometric contours from areas of higher head to lower head. The spacing of contours indicates the hydraulic gradient: tight spacing means steep gradient (high flow velocity), wide spacing indicates gentle gradient. Closed contours (highs or lows) can indicate recharge mounds or discharge depressions.

5. **Corrections**: For aquifers with variable density (e.g., coastal or brine interfaces), head values may be corrected to freshwater equivalent. In confined aquifers, the potentiometric surface often lies above the aquifer top.

## Variants

- **Water-Table Contour Map**: Used for unconfined (phreatic) aquifers. The surface is the actual water table. Contours represent the elevation of the water table, and flow direction is generally horizontal toward streams or wells.

- **Piezometric Contour Map**: Applied to confined or semi-confined aquifers. The contour represents the pressure surface (potentiometric surface) which may be above or below the land surface (artesian conditions).

- **Head Difference Maps**: Contours of change in hydraulic head over time (e.g., pre- and post-pumping), used to assess drawdown or recovery.

- **Flow Nets**: Combine potentiometric contours with flow lines to create a grid-like network for analyzing seepage quantities and velocities.

- **Isopach/Potential Maps**: In some contexts, potentiometric contours can be combined with aquifer thickness (isopachs) to compute transmissivity or groundwater flux.

## Trade-offs

- **Data Density**: Sparse well networks produce uncertain contours, especially in heterogeneous aquifers. More wells improve accuracy but increase monitoring costs.

- **Temporal Variability**: Potentiometric surfaces fluctuate due to seasonal recharge, pumping, or tidal effects. A single synoptic survey may not represent average conditions; repeated surveys across different seasons are often needed.

- **Interpolation Errors**: Contours are only as good as the interpolation method. Geostatistical methods (kriging) account for spatial correlation but require sufficient data. Simple methods may oversmooth or create unrealistic artifacts (e.g., bull’s-eyes).

- **Vertical Head Variations**: In multilayered aquifers, separate potentiometric surfaces exist for each layer. Averaging head measurements from wells screened across multiple zones can create misleading contours.

- **Well Construction Effects**: Wells with long screens or open intervals may measure a mixed head, not representative of a discrete depth. Proper well construction and screening are critical.

- **Scale and Resolution**: Large contour intervals can obscure local features; too small intervals may amplify noise. The choice of contour interval must balance clarity and detail.

## See also

- Potentiometric Surface  
- Water Table  
- Hydraulic Head  
- Contour Map  
- Groundwater Monitoring  
- Flow Net  
- Kriging (geostatistics)  
- Drawdown