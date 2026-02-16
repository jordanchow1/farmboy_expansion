# Farm Boy Market Analysis

> Comprehensive demographic and geographic analysis of Farm Boy store locations across Ontario, Canada

## Overview

This project analyzes the demographic characteristics and geographic distribution of **51 Farm Boy grocery store locations** across Ontario. By merging store location data with Statistics Canada 2021 Census data at the Forward Sortation Area (FSA) level, we identify key market patterns, demographic preferences, and expansion opportunities.

### Business Questions Answered:

- What is the typical Farm Boy market demographic profile?
- How do population, density, and age vary across store locations?
- Which regions and market types does Farm Boy target?
- What are the characteristics of high-performing markets?
- Where are the best opportunities for expansion?

## Key Findings

### Market Profile

| Metric | Value |
|--------|-------|
| **Total Stores** | 51 |
| **Total Population Served** | 1,810,313 |
| **Average FSA Population** | 35,496 |
| **Average Population Density** | 3,900 per sq km |
| **Median Customer Age** | 40.2 years |

### Strategic Insights

✅ **Market Sweet Spot:**
- Population: 30,000-45,000
- Density: 1,500-3,500 people per sq km
- Median Age: 38-42 years
- Market Type: Medium to high-density suburban

✅ **Geographic Distribution:**
- 35% Eastern Ontario (Ottawa region)
- 27% GTA/Golden Horseshoe
- 22% Toronto
- 16% Southwestern Ontario

✅ **Demographic Focus:**
- 73% of stores target age 35-45 demographic
- 78% are in medium to high-density markets
- Strong preference for mature, family-oriented communities

## Dataset

### Data Sources

1. **Store Location Data**
   - 51 Farm Boy store locations
   - Store names and full addresses
   - Extracted FSA codes from postal codes

2. **Census Data (Statistics Canada 2021)**
   - Population by FSA
   - Land area (sq km)
   - Median age of population
   - Population density

### Data Structure

```
merged_data.csv
├── Store Name          (string)
├── Address            (string)
├── FSA                (string - 3 characters)
├── PRNAME             (string - Province name)
├── LANDAREA           (float - sq km)
├── Median age         (float - years)
├── Population, 2021   (float - count)
└── population_density (float - per sq km)
```

### FSA Code Reference

Ontario FSA prefixes indicate region:
- **K** - Eastern Ontario (Ottawa, Kingston)
- **L** - GTA/Golden Horseshoe (Mississauga, Hamilton, etc.)
- **M** - Toronto
- **N** - Southwestern Ontario (London, Windsor, etc.)
- **P** - Northern Ontario (Sudbury, Thunder Bay)

## Analysis Components

### 1. Descriptive Statistics
- Summary statistics for all demographic variables
- Distribution analysis (mean, median, quartiles)
- Variance and standard deviation calculations

### 2. Market Categorization
- **Density Categories:** Low, Medium, High, Very High
- **Age Categories:** Young (<35), Middle (35-45), Mature (45-55), Older (55+)
- **Regional Groupings:** By FSA prefix

### 3. Regional Analysis
- Store distribution by region
- Average demographics per region
- Regional comparison visualizations

### 4. Market Segmentation
- Quadrant analysis (Population × Density)
- High-value market identification
- Expansion opportunity mapping

### 5. Correlation Analysis
- Relationships between variables
- Density vs. age patterns
- Population vs. market characteristics

## Visualizations

### Generated Outputs

1. **`farm_boy_dashboard_summary.png`**
   - Executive dashboard with key metrics
   - Market type distribution pie chart
   - Regional breakdown bar chart
   - Top markets tables

2. **`farm_boy_complete_analysis.png`**
   - 9-panel comprehensive visualization
   - Population, density, and age distributions
   - Market type and age category breakdowns
   - Regional comparisons
   - Scatter plots showing relationships

3. **`farm_boy_regional_comparison.png`**
   - Box plots by region
   - Population distribution comparison
   - Density distribution comparison
   - Age demographics by region
   - Stacked bar charts

4. **`farm_boy_market_insights.png`**
   - Top 15 markets by population
   - Top 15 markets by density
   - Correlation heatmap
   - Market segmentation scatter plot

## 🔬 Methodology

### 1. Data Collection
- Store addresses geocoded to FSA level
- Census data aggregated at FSA level
- Data merged on FSA code

### 2. Data Cleaning
- FSA extraction from postal codes using regex: `[A-Z]\d[A-Z]`
- Validation of FSA codes against Ontario prefixes
- Handling of missing values

### 3. Feature Engineering
- **Population Density:** Population ÷ Land Area
- **Density Categories:** Quartile-based binning
- **Age Categories:** Custom bins based on business logic
- **Regional Labels:** Mapping from FSA prefix

### 4. Statistical Analysis
- Descriptive statistics for all variables
- Quartile analysis for market segmentation
- Correlation analysis between key metrics
- Regional aggregation and comparison

### 5. Visualization
- Multi-panel matplotlib figures
- Box plots for distribution comparison
- Scatter plots for relationship analysis
- Heatmaps for correlation matrices

## Results

### Market Characteristics

**Population Distribution:**
- Minimum: 10,332
- Q1: 19,499
- **Median: 32,046**
- Q3: 43,894
- Maximum: 100,835

**Density Distribution:**
- Minimum: 236 per sq km
- Q1: 1,305 per sq km
- **Median: 2,005 per sq km**
- Q3: 3,178 per sq km
- Maximum: 31,245 per sq km

**Age Distribution:**
- Minimum: 31.4 years
- Q1: 38.0 years
- **Median: 40.0 years**
- Q3: 42.2 years
- Maximum: 48.0 years

### Market Type Distribution

| Category | Stores | Percentage |
|----------|--------|------------|
| Low Density (<500) | 3 | 5.9% |
| Medium Density (500-2,000) | 22 | 43.1% |
| High Density (2,000-5,000) | 18 | 35.3% |
| Very High Density (>5,000) | 8 | 15.7% |

### Top 5 Markets

**By Population:**
1. Mapleview (Barrie) - 100,835
2. Greenbank - 81,863
3. Oakwoods - 72,662
4. Tenth Line - 62,125
5. Aurora - 62,061

**By Density:**
1. College and Bay - 31,245 per sq km
2. Sugar Wharf - 23,791 per sq km
3. Front and Bathurst - 15,626 per sq km
4. Metcalfe - 14,378 per sq km
5. Yonge and Soudan - 9,988 per sq km

## Acknowledgments

- **Statistics Canada** for providing 2021 Census data
- **Farm Boy** for store location information

## References

- [Statistics Canada 2021 Census](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/index-eng.cfm)
- [FSA Geographic Information](https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/postal-codes.page)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
