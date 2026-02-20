# Farm Boy Expansion Strategy  
Predictive Demographic & Spatial Modeling for Retail Site Selection

---

## Executive Summary

Farm Boy’s current Ontario footprint is heavily concentrated in the GTA and Ottawa, creating clustering risk and limiting visibility into true whitespace opportunity.

This project builds a **probability-driven expansion framework** that integrates demographic profiling, geographic controls, and logistic regression modeling to systematically identify high-potential Forward Sortation Areas (FSAs) across Ontario.

Rather than relying on heuristic thresholds (e.g., population bands or density cutoffs), this model estimates the likelihood that any Ontario FSA resembles existing Farm Boy trade areas, while controlling for spatial saturation effects.

The result is a ranked list of expansion-ready FSAs grounded in statistical alignment and geographic discipline.

---

## Strategic Framing

### The Problem

Traditional expansion analysis risks:
- Overweighting dense urban clusters
- Mistaking proximity for demand
- Ignoring cannibalization risk
- Relying on static demographic thresholds

Given Farm Boy’s clustered footprint, descriptive analysis alone is insufficient.

---

### The Solution

This project introduces a three-layer expansion framework:

1. **Demographic Benchmarking**  
   Identify the empirical profile of existing store FSAs.

2. **Geographic Control Layer**  
   Adjust for clustering and proximity bias using distance metrics and regional segmentation.

3. **Logistic Regression Probability Model**  
   Estimate expansion suitability across all 520 Ontario FSAs using supervised classification.

---

## Model Outcome

The logistic regression model:

- Quantifies demographic alignment
- Penalizes oversaturated proximity
- Identifies statistically similar but underserved FSAs
- Produces expansion probability scores for the entire province

High-potential FSAs were selected using a defined probability threshold and distance safeguards.

---

## Top 10 High-Potential FSAs (Logistic Regression Ranked)

Based on predicted probability scores from the logistic regression model, the following FSAs exhibit the strongest statistical alignment with existing Farm Boy locations while satisfying geographic control criteria:

| Rank | FSA | Region  | Predicted Probability |
|------|-----|---------|----------------------|
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

---

### Interpretation

These FSAs:

- Strongly resemble the demographic profile of current Farm Boy trade areas  
- Maintain sufficient separation from oversaturated clusters  
- Score highest in probability-based suitability modeling  

The concentration of high-scoring FSAs in Ottawa suggests:
- Continued depth opportunity within the Ottawa region
- Potential micro-cluster optimization strategy
- Need for cannibalization analysis before deployment

GTA candidates (L5M, L6M) represent selective suburban expansion potential rather than dense urban infill.

---

These ranked FSAs represent statistically defensible expansion candidates derived from supervised predictive modeling rather than heuristic screening.
