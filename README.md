# SectionA_Group7_RoadAccidents Capstone Project

This repository contains the capstone project for Section A, Group 7, focusing on Road Accidents analysis.

## Project Structure

- `data/`: Contains datasets
  - `raw/`: Original datasets (never edited)
  - `processed/`: Cleaned output data
- `notebooks/`: Jupyter notebooks for analysis
  - `01_extraction.ipynb`: Data extraction
  - `02_cleaning.ipynb`: Data cleaning
  - `03_eda.ipynb`: Exploratory Data Analysis
  - `04_statistical_analysis.ipynb`: Statistical analysis
  - `05_final_load_prep.ipynb`: Final load preparation
- `scripts/`: Python scripts
  - `etl_pipeline.py`: ETL pipeline script
- `tableau/`: Tableau visualizations
  - `screenshots/`: Dashboard screenshots
  - `dashboard_links.md`: Links to dashboards
- `reports/`: Project deliverables
  - `project_report.pdf`: Project report
  - `presentation.pdf`: Presentation slides
- `docs/`: Documentation
  - `data_dictionary.md`: Data dictionary
- `DVA-oriented-Resume`: Resume focused on DVA
- `DVA-focused-Portfolio`: Portfolio focused on DVA

## Getting Started

[Add instructions here]

## Authors

Section A, Group 7
- Suhaani Garg
- Krishna dave
- Keshav
- Sathvik
- Anushka
- Arya Pandey
- Hardik Maheshwari

## Contributions
### Krishna Dave
#### Driver Risk Analysis

Interactive Tableau dashboard analyzing how driver demographics 
affect road accident severity.

### Covers
- Age vs Severity
- Driving Experience vs Severity  
- Gender vs Severity
- Age × Experience Heatmap
- Weekend vs Weekday Risk

### Key Insight
Inexperienced and young drivers form the highest-risk segment across all severity levels.


### Anushka Tyagi
#### Road Accident Dashboard Analysis
Designed interactive Tableau dashboards to analyze accident severity, driver risk, and overall incident patterns, and presented the insights through a PPT.

### Covers
- Accident Severity Analysis
- Driver Profile & Risk Patterns
- Accident Risk & Contributing Factors
- Severity distribution across different conditions

### Key Insight
Accident severity and risk are heavily influenced by driver profiles and external conditions, with clear patterns across different scenarios.

### Sathvik Koriginja
#### Data Cleaning & Dashboard Development

Handled data preparation and visualization for the project. Cleaned, transformed, and structured raw accident data to ensure accuracy and usability for analysis, and built an interactive Tableau dashboard to present key insights.

Covers
- Data extraction and preprocessing
- Handling missing values and inconsistencies
- Feature engineering for analysis
- Preparing final dataset for visualization
- Building Accident Risk & Severity Dashboard in Tableau

### Key Insight
Clean and well-structured data enabled accurate identification of accident patterns, highlighting that road conditions, vehicle movement, and collision types play a major role in severity outcomes.

### Suhaani Garg
#### Data Preparation, Dashboard Development & Report Contribution

Contributed across multiple stages of the project including data preprocessing, dashboard development, and reporting. Played a key role in refining datasets, improving dashboard quality, and ensuring consistency in the final analysis.

### Covers
- Assisted in data cleaning and preprocessing using Google Colab (Python)
- Contributed to final dataset preparation and load pipeline in Python (`05_final_load_prep.ipynb`)
- Designed and developed Dashboard 4 in Tableau
- Improved dashboard structure, layout, and interactivity
- Ensured data accuracy and consistency across visualizations
- Assisted in final project report and documentation

### Key Insight
Accurate data preprocessing combined with well-structured dashboards improves the clarity, reliability, and interpretability of accident analysis, enabling better understanding of risk patterns and contributing factors.

### Arya Pandey
#### Visualization Design, Dashboard Development & Integration

Led the design and development of interactive Tableau dashboards, focusing on transforming processed data into clear, analytical visualizations. Played a key role in structuring dashboards, refining chart selection, and ensuring consistency across all visual outputs.

### Covers
- Designed and developed Severity Overview Dashboard
- Built Time & Pattern Analysis Dashboard
- Created key visualizations including:
  - Accident Frequency by Hour
  - Day of Week Trends
  - Hour × Day Heatmap
  - Severity by Weather Conditions
  - Road Surface vs Severity
  - Casualties vs Severity
- Applied effective visualization techniques for better analytical clarity
- Standardized color schemes, sorting, and labeling across dashboards
- Integrated multiple dashboards into a unified Tableau workbook
- Resolved data source and extract issues during collaboration
- Ensured dashboards follow a clear storytelling structure

### Key Insight
Accident patterns are highly time-dependent, with clear peaks during rush hours and consistent high-risk time windows. Combining temporal trends with environmental and severity analysis shows that accidents follow predictable patterns influenced by human behavior and traffic conditions.


### H Maheshwari
#### EDA & Statistical Analysis Lead

Led the analytical phase of the project by conducting in-depth Exploratory Data Analysis (EDA), statistical evaluation, and KPI computation using Python.

### Covers
- Performed comprehensive **Exploratory Data Analysis (EDA)** on the cleaned dataset *(Notebook 03)*  
- Conducted **statistical analysis and pattern validation** *(Notebook 04)*  
- Analyzed relationships between features and accident severity using **univariate and bivariate techniques**  
- Computed key **KPIs and risk indicators** for decision-making  
- Identified **temporal, behavioral, and environmental patterns** influencing accident severity  
- Generated insights to support **dashboard design and final reporting**

### Key Insight
Accident severity is driven more by **behavioral factors (driver actions, experience, and timing)** than environmental conditions, with clear risk spikes during **evening hours and weekends**, and higher severity associated with specific driver and collision patterns.

