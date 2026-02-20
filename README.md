# Farm Boy Expansion Strategy  
Predictive Demographic & Spatial Modeling for Retail Site Selection

---

## Executive Summary

Farm Boy’s current Ontario footprint is heavily concentrated in the GTA and Ottawa, creating clustering risk and limiting visibility into true whitespace opportunity.

This project builds a **probability-driven expansion framework** that integrates demographic profiling, geographic controls, and logistic regression modeling to systematically identify high-potential Forward Sortation Areas (FSAs) across Ontario.

Rather than relying on heuristic thresholds (e.g., population bands or density cutoffs), this model estimates the likelihood that any Ontario FSA resembles existing Farm Boy trade areas — while controlling for spatial saturation effects.

The result is a ranked, defensible list of expansion-ready FSAs grounded in statistical alignment and geographic discipline.

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
