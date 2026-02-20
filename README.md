# Farm Boy Market Analysis

> Demographic & geographic analysis of 51 Farm Boy store locations across Ontario, Canada, with regional clustering controls.

## Overview

Analyze Farm Boy store locations with 2021 Census data at the FSA level to identify:  
- Market demographics & preferences  
- High-value areas & expansion opportunities  
- Geographic effects on store performance  

**New:** Introduced a **Geographic Control Layer** to account for clustering and regional saturation.

## Business Questions

- Typical Farm Boy customer demographic?  
- How do population, density, and age vary across locations?  
- How does proximity to existing stores influence opportunities?  
- Where are underpenetrated markets for expansion?

## Key Insights

- **Market Sweet Spot:** 30k–45k population, 1,500–3,500 people/km², median age 38–42  
- **Demographic Focus:** 35–45 age, medium/high-density suburban areas  
- **Geographic Control Layer:**  
  - Distance-to-nearest-store variable introduced  
  - Optional region dummies: GTA, Ottawa, Other Ontario  
  - Demographic trends persist after accounting for clustering  

## Dataset

- **Store Data:** 51 locations, FSA codes, addresses  
- **Census Data:** Population, land area, density, median age  

**New Feature:** `distance_to_nearest_store` (km)  

## Analysis Workflow

1. **Descriptive Stats:** Means, medians, quartiles  
2. **Market Categorization:** Density & age bins, regional groupings  
3. **Regional Analysis:** Compare demographics by region  
4. **Geographic Control Layer:** Adjust for clustering, identify saturated vs underpenetrated FSAs  
5. **Segmentation & Correlation:** Population × density quadrants, correlation matrices  
6. **Visualization:** Scatter plots, boxplots, heatmaps  

## Visuals

![Correlation Matrix](https://github.com/jordanchow1/farmboy_expansion/blob/main/correlation_matrix.png)  
![Regional Comparison](https://github.com/jordanchow1/farmboy_expansion/blob/main/regional_comparison.png)  

## Results Snapshot

- **Median Population:** 32,046  
- **Median Density:** 2,005/km²  
- **Median Age:** 40  
- **High-density clusters:** College & Bay (31,245/km²), Sugar Wharf (23,791/km²)  
- **Population hotspots:** Mapleview (100,835), Greenbank (81,863)  
- Distance-to-nearest-store reveals regional saturation and expansion potential  

## Acknowledgments

- **Statistics Canada** – Census 2021  
- **Farm Boy** – Store data  

## References

- [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm)  
- [FSA Geographic Info](https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/postal-codes.page)  
