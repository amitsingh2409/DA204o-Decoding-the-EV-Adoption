# DA204o-Decoding-the-EV-Adoption

## Background of the problem​
The project highlights the need for sustainable transportation options, with EVs emerging as a promising solution.​

## Why is it important? ​
EV adoption is crucial for climate change mitigation, policy development, infrastructure planning, market insights, urban planning, consumer education, and understanding economic impacts.​

## Objectives of the project​
Key goals include conducting comprehensive EDA, developing predictive models, analyzing geographical patterns, creating visualization tools, and generating actionable insights.​

## How can Data Science solve the problem?​
### Exploratory Data Analysis (EDA)
Analyze the dataset to identify trends and patterns in EV adoption across different regions. For example, examining the distribution of EV types (all-electric vs. plug-in hybrid) and their electric ranges.​

### Predictive Modeling
Develop machine learning models to predict the EV type and which would be useful to have an idea of the demand for charging infrastructure in different regions.​

### Geospatial Analysis
Use the geographic information (County, City, State, Postal Code, Vehicle Location) to perform geospatial analysis.​

### Visualization Tools
Create interactive dashboards and visualizations to communicate insights effectively. For example, maps showing EV adoption density by county or city, and charts displaying trends over model years.​

### Consumer Behavior Analysis
Analyze the dataset to understand consumer preferences and barriers to adoption. For example, examining the relationship between base MSRP and electric range to identify factors influencing purchasing decisions.​

## Data source(s)
It is a new dataset sourced on 20 September 2024 which shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL). Electric Vehicle Population Data - Catalog​

## Description of the data
The dataset contains 17 columns:​
- VIN (1-10): Vehicle Identification Number (categorical)​
- County: Registration county (categorical)​
- City: Registration city (categorical)​
- State: Registration state (categorical)​
- Postal Code: Registration postal code (numerical - float)​
- Model Year: Vehicle manufacture year (numerical - int)​
- Make: Vehicle manufacturer/brand (categorical)​
- Model: Specific vehicle model (categorical)​
- EVType: Electric vehicle classification (categorical)​
- CAFV: Clean Alternative Fuel Vehicle eligibility (categorical)​
- Electric Range: Maximum electric-only travel distance in miles (numerical - float)​
- Base MSRP: Manufacturer's Suggested Retail Price (numerical - float)​
- Legislative District: Registration legislative district (numerical - float)​
- DOL Vehicle ID: Department of Licensing identifier (numerical - int)​
- Vehicle Location: Specific registration location details (categorical)​
- Electric Utility: Power provider for the vehicle's location (categorical)​
- 2020 Census Tract: Census geographic area identifier (numerical - float)​

## Any preprocessing steps required
- Handling missing values
- Feature engineering and scaling
- Detecting and handling outliers
- Data Splitting for modeling​

## Overview of Methods or Models You Plan to Use​
### Exploratory Data Analysis (EDA)​
- Analyze trends and patterns in EV adoption across different regions.​
- Examine the distribution of EV types and their electric ranges.​
- Identify correlations between features such as base MSRP and electric range.​

### Predictive Modeling​
- Develop machine learning models to predict the EV type and which would be useful to have an idea of the demand for charging infrastructure in different regions.​

### Geospatial Analysis​
- Use geographic information to analyze spatial patterns in EV adoption.​
- Identify regions with high or low EV adoption density.​

### Visualization Tools​
- Use maps to show EV adoption density by county or city.​

### Consumer Behavior Analysis​
- Analyze consumer preferences and barriers to adoption.​
- Examine the relationship between base MSRP and electric range.​

## Justification for Choosing These Methods​
- EDA: Essential for understanding the dataset and identifying initial trends and patterns.​
- Predictive Modeling: Helps in forecasting future trends and making data-driven decisions.​
- Geospatial Analysis: Provides insights into regional adoption patterns, crucial for infrastructure planning.​
- Visualization Tools: Effective communication of insights to stakeholders.​
- Consumer Behavior Analysis: Understanding consumer preferences aids in policy development and market strategies.​

## Tools/Technologies​
- Pandas, NumPy: Numerical operations
- Matplotlib & Seaborn: Data visualization
- Scikit-learn: Machine learning
- GeoPandas: Geospatial analysis
- Plotly & Dash: Interactive visualizations