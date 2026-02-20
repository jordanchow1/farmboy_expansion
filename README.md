# Farm Boy Market Analysis

Comprehensive **demographic, geographic, and spatial analysis** of 51 Farm Boy grocery store locations across Ontario, Canada, with a **Geographic Control Layer** added to account for clustering and regional saturation effects.

---

## Overview

This project analyzes market characteristics and expansion opportunities for Farm Boy by combining:

- Geocoded store locations  
- 2021 Statistics Canada Census data (FSA-level)  
- Engineered spatial variables  

Rather than evaluating demographics alone, this analysis isolates **true market potential** from spatial saturation effects.

---

## Business Questions

- What defines the typical Farm Boy trade area?
- How do population, density, and age vary across store locations?
- How clustered are current store locations?
- Which FSAs show expansion potential after controlling for proximity effects?
- Do demographic drivers remain significant once spatial controls are included?

---

## Geographic Control Layer

### Why It Matters

Stores are heavily clustered in the GTA and Ottawa. Without controlling for geography, demographic analysis can misidentify opportunity due to regional concentration.

The Geographic Control Layer corrects for this.

### Spatial Variables Added

- `distance_to_nearest_store` (km) — calculated using the Haversine formula  
- Regional dummy variables:
  - GTA  
  - Ottawa  
  - Other Ontario  

### What It Enables

- Identification of saturation zones  
- Separation of demographic attractiveness from geographic clustering  
- Detection of underpenetrated but demographically aligned FSAs  
- More defensible, data-driven expansion recommendations  

---

## Market Profile Findings

### Core Demographic Sweet Spot

- **Population:** 30,000–45,000  
- **Density:** 1,500–3,500 people/km²  
- **Median Age:** 38–42  

Farm Boy locations are concentrated in medium-to-high density suburban markets with mature, family-oriented demographics.

---

## Spatial Insights

After controlling for proximity and region:

- Demographic signals remain strong  
- High-density urban cores show clustering saturation  
- Several mid-density FSAs outside major clusters emerge as expansion candidates  
- Distance-based analysis prevents overestimating demand in already saturated zones  

---

## Data Sources

### Store Data
- 51 Farm Boy locations  
- Geocoded to FSA level  

### Census Data (2021)
- Population  
- Land area  
- Population density  
- Median age  

Source: Statistics Canada 2021 Census

---

## Methodology

1. Data cleaning and geocoding  
2. FSA-level demographic aggregation  
3. Haversine distance calculation  
4. Regional segmentation (GTA, Ottawa, Other)  
5. Market categorization (population × density bins)  
6. Correlation and spatial control analysis  
7. Visualization and summary metrics  

---

## Key Metrics

- **Median Population:** ~32,046  
- **Median Density:** ~2,005 people/km²  
- **Median Age:** ~40 years  
- **Total Ontario FSAs analyzed:** 520  
- **Total Store Locations:** 51  
---

## Business Recommendations

Using the ranked list of underserved FSAs (`underserved_fsas_ranked.csv`), expansion strategy should prioritize markets that:

- Match Farm Boy’s demographic sweet spot  
- Are materially distant from existing stores  
- Sit outside high-saturation GTA clusters  
- Exhibit strong population–density balance  

### 1. Tiered Expansion Strategy

#### Tier 1: Immediate Feasibility Assessment
Top-ranked FSAs with:
- High demographic alignment (population + density within target band)
- Strong distance from nearest existing store
- Mid-to-large population base

**Action:**  
Conduct micro-site feasibility studies, including:
- Real estate availability
- Traffic flow analysis
- Retail co-tenancy mapping
- Household income validation

These FSAs represent the highest-probability expansion candidates.

---

#### Tier 2: Medium-Term Pipeline Markets
FSAs that:
- Slightly miss one demographic threshold (e.g., density just below ideal range)
- Are geographically strategic (bridge markets between clusters)

**Action:**  
Monitor population growth trends and housing development permits.  
These areas may become optimal within 2–3 years.

---

#### Tier 3: Strategic Regional Diversification
FSAs located:
- Outside GTA/Ottawa clusters  
- In mid-sized Ontario markets  
- With strong demographic alignment but historically underpenetrated

**Action:**  
Pilot 1–2 stores to test regional elasticity and brand transferability.

This reduces long-term overexposure to GTA saturation risk.

---

## Geographic Risk Management

The Geographic Control Layer reveals that:

- Current store density is heavily clustered.
- Marginal returns in saturated urban cores are likely diminishing.
- Distance-adjusted opportunity scores better predict whitespace.

### Recommendation:
Adopt a **minimum distance threshold policy** for new stores (e.g., X km from existing location unless in ultra-high-density core zones).

This institutionalizes spatial discipline into site selection.

---

## Capital Allocation Framework

Allocate expansion capital using a weighted scoring model:

- 40% Demographic Fit  
- 30% Distance from Existing Stores  
- 20% Regional Diversification Value  
- 10% Growth Indicators (housing starts, migration trends)

This formalizes expansion decisions and reduces subjective bias.

---

## Strategic Conclusion

The Geographic Control Layer strengthens expansion decisions by separating:
- True demographic demand  
- From geographic clustering bias  

The ranked underserved FSAs represent disciplined, data-driven expansion targets rather than opportunistic site selection.

This framework moves expansion planning from descriptive analytics to structured spatial strategy.

---

## Visuals
![correlation_matrix](https://github.com/jordanchow1/farmboy_expansion/blob/main/correlation_matrix.png)
![regional_comparison](https://github.com/jordanchow1/farmboy_expansion/blob/main/regional_comparison.png)

## References

- Statistics Canada 2021 Census  
- Canada Post FSA geographic reference data  
