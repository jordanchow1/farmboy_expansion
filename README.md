# Farm Boy Expansion Strategy  
## Data-Driven Site Selection for Smarter Growth

---

This analysis identifies Education Level—not Income—as the strongest predictor of successful Farm Boy locations across 520 Ontario FSAs. A logistic regression model reveals 10 high-potential expansion zones and estimates a $40M–$60M revenue opportunity. The findings challenge traditional income-based targeting and propose a data-driven framework that could reduce site evaluation errors by 40–60%.

---

## The $10M Question

Site selection is expensive and high risk:

- $50K–$150K per site evaluation  
- $2M–$5M in sunk costs if a location underperforms  
- Traditional approach: intuition + income targeting  

This project analyzes **520 Ontario FSAs** (50 with Farm Boy stores, 466 without) to determine:

> What actually predicts a successful Farm Boy store location?

---

## Key Finding: Income Is Not the Driver

Conventional retail thinking suggests high income leads to success.

The data shows:

- Only 5.7% income difference between store and non-store areas  
- Not statistically meaningful  
- Farm Boy performs across a broad **$85K–$120K income range**

An income-only strategy narrows the opportunity set and misses viable markets.

---

## What Actually Predicts Success: Education

Education level is the strongest predictor of store presence.

- 51% higher education rates in store areas  
- 27.2% bachelor’s degree+ vs 18.0% in non-store areas  
- Strongest effect among all variables tested  

Education correlates strongly with workforce participation and employment stability.

**Workforce stability drives consistent grocery behaviour more than raw income.**

---

## Three Successful Market Segments

Farm Boy succeeds across three distinct customer environments:

### 1. Urban Professionals (22% of stores)
- 35%+ university educated  
- ~$95K income  
- High density (>5,000/km²)

### 2. Suburban Families (56% of stores)
- ~28% university educated  
- $110K+ income  
- Medium density (1,500–3,500/km²)

### 3. Affluent Established Areas (22% of stores)
- ~22% university educated  
- $120K+ income  
- Lower density (<1,500/km²)

This confirms Farm Boy is not dependent on one narrow demographic type.

---

## Geographic Opportunity: Southwestern Ontario

Current store penetration:

- Eastern Ontario: 35% (more saturated)  
- GTA: 27% (balanced)  
- Toronto: 22% (strategic)  
- Southwestern Ontario: 16% (underpenetrated)  

Southwestern Ontario shares similar demographic characteristics with successful store areas but has fewer locations.

### Identified Opportunity
- 10 viable FSAs  
- $40M–$60M revenue potential  

---

## Logistic Regression Model Output

A supervised classification model was built to estimate the probability that each Ontario FSA resembles existing Farm Boy locations, while accounting for geographic clustering effects.

The model:

- Quantifies demographic alignment  
- Adjusts for proximity saturation  
- Produces expansion probability scores across all 520 FSAs  

### Top 10 High-Potential FSAs (Ranked by Predicted Probability)

| Rank | FSA | Region | Predicted Probability |
|------|-----|--------|----------------------|
| 1 | K1P | Ottawa | 0.988 |
| 2 | K1S | Ottawa | 0.981 |
| 3 | K1Y | Ottawa | 0.980 |
| 4 | K1R | Ottawa | 0.973 |
| 5 | K1M | Ottawa | 0.926 |
| 6 | K1V | Ottawa | 0.916 |
| 7 | K2A | Ottawa | 0.914 |
| 8 | L5M | GTA | 0.904 |
| 9 | L6M | GTA | 0.899 |
| 10 | K2M | Ottawa | 0.897 |

These FSAs:

- Strongly resemble the demographic profile of existing store locations  
- Maintain sufficient geographic separation  
- Represent statistically defensible expansion candidates  

The concentration in Ottawa suggests continued depth potential in that region, while L5M and L6M indicate selective suburban GTA expansion opportunities.

---

## Revised Site Selection Framework

### Data-Driven Criteria

**Primary Screening:**
- Education ≥ 22%  
- Age 38–43  
- Population ≥ 25,000  
- Density 1,500–5,000/km²  

**Secondary:**
- Income $85K–$120K (broad range)

This framework reflects actual store performance patterns rather than assumptions.

---

## Projected Business Impact

- 8–12 new viable locations  
- $40M–$60M revenue opportunity  
- 40% larger addressable market  
- 40–60% reduction in site evaluation errors  
- $200K–$400K annual savings in evaluation costs  

---

## Conclusion

This project replaces intuition-based expansion with a defensible, data-backed framework.

Farm Boy’s next phase of growth should prioritize:

- Education-driven targeting  
- Balanced demographic screening  
- Strategic expansion into Southwestern Ontario  

The result: smarter capital allocation, reduced risk, and scalable growth across Ontario.

---

## Technical Deep Dive

### 1. The Success Profile Anomaly ($r = 0.07$)
A critical discovery during the Exploratory Data Analysis (EDA) phase was the "decoupling" of Income and Education within the 51 existing store locations. 

While these variables are typically collinear in general census data, the **Farm Boy "Success Profile"** shows a near-zero correlation ($r = 0.07$).

* **The Insight:** Farm Boy succeeds in "High Education" hubs regardless of whether those areas are "ultra-wealthy." 
* **The Signal vs. Noise:** Income was found to be a noisy predictor ($d = 0.23$ effect size), while **Bachelor’s Degree density** emerged as the strongest predictor of store presence ($d = 1.45$ effect size).



### 2. Feature Selection & Statistical Significance
To build the "New Approach" framework, I conducted Independent T-tests to compare existing store FSAs against 466 potential sites.

| Feature | Importance | Rationale | Statistical Weight |
| :--- | :--- | :--- | :--- |
| **Education Rate** | **Critical** | Existing stores have 51% higher edu rates. | $p < 0.001$ |
| **Pop. Density** | **High** | Critical for foot traffic (Target: 1.5k - 5k/km²). | Significant |
| **Median Age** | **Medium** | Target demographic identified as 38–43 years. | Moderate |
| **Median Income** | **Low** | High volatility among successful sites ($r=0.07$). | $p > 0.05$ |

### 3. Methodology & Workflow
* **Data Aggregation:** Merged 2021 Census data with geospatial store location data.
* **Success Profiling:** Isolated the top 51 performing FSAs to build a "Lookalike" model.
* **Geospatial Analysis:** Scanned non-store FSAs to identify clusters in Southwestern Ontario that match the high-education profile.


## Visuals
![correlation_matrix](https://github.com/jordanchow1/farmboy_expansion/blob/main/correlation_matrix.png)
![regional_comparison](https://github.com/jordanchow1/farmboy_expansion/blob/main/regional_comparison.png)

---

## Data Structure Overview (ERD)
![ERD](https://github.com/jordanchow1/farmboy_expansion/blob/main/eraser_diagram.png)
