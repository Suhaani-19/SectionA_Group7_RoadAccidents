# NST DVA Capstone 2 — Road Accident Severity Analysis

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw road accident data into actionable public safety intelligence.

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Road Accident Severity Analysis |
| **Sector** | Public Safety & Transportation |
| **Team ID** | SectionA-Group7 |
| **Section** | Section A |
| **Faculty Mentor** | Newton School of Technology DVA Faculty |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 2025 |

### Team Members

| Role | Name | Portfolio |
|---|---|---|
| Project Lead | Suhaani Garg | [🌐 Portfolio](https://suhaani-19.github.io/Data_Analytics_Portfolio/) |
| Strategy Lead | Krishna Dave | [🌐 Portfolio](https://krishna-dave206.github.io/DVAPortfolio/) |
| ETL Lead | Sathvik Koriginja | [🌐 Portfolio](https://sathvik89.github.io/DVA_Portfollio/) |
| Analysis Lead | Hardik Maheshwari | [🌐 Portfolio](https://hardikgenone.github.io/dva-portfolio/) |
| PPT & Quality Lead | Anushka Tyagi | [🌐 Portfolio](https://anu-ushka.github.io/DataAnalytics_Portfolio/) |
| Data Lead | Keshav Rajput | [🌐 Portfolio](https://dva-portfolio-sand.vercel.app/) |
| Visualization Lead | Arya Pandey | [🌐 Portfolio](https://arya-p-gh.github.io/DVA_PORTFOLIO/) |

---

## Business Problem

Road traffic accidents are a leading cause of injury and death globally, yet the patterns driving severity remain poorly understood by policymakers and traffic authorities. This project analyzes a real-world road accident dataset to identify the behavioral, environmental, and temporal factors that most strongly predict accident severity. The analysis is designed to serve traffic safety officers, urban planners, and public health decision-makers who need evidence-based guidance on where and how to intervene.

**Core Business Question**

> Which driver, road, time, and environmental factors most strongly predict whether a road accident results in a slight, serious, or fatal injury — and where should authorities focus prevention efforts?

**Decision Supported**

> This analysis enables traffic safety authorities to prioritize enforcement, infrastructure investment, and awareness campaigns by identifying the highest-risk driver profiles, time windows, road conditions, and collision types.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Road Traffic Accident (RTA) Dataset |
| **Direct Access Link** | [Kaggle — RTA Dataset](https://www.kaggle.com/) |
| **Row Count** | 12,295 (after cleaning) |
| **Column Count** | 22 (18 original + 4 derived) |
| **Time Period Covered** | Cross-sectional accident records |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `Accident_severity` | Severity level: slight / serious / fatal injury | Target variable, KPI, all dashboards |
| `Age_band_of_driver` | Driver age group (e.g. 18–30, 31–50) | Segmentation, risk profiling |
| `Driving_experience` | Years of driving experience | Risk factor, bivariate analysis |
| `Cause_of_accident` | Primary cause (e.g. overtaking, no distancing) | Cause analysis dashboard |
| `Hour` / `Time_period` | Hour extracted from time; period derived | Temporal analysis, heatmap |
| `Day_of_week` / `is_weekend` | Day of accident; weekend flag derived | Weekend vs weekday KPI |
| `Weather_conditions` | Weather at time of accident | Environmental risk analysis |
| `Light_conditions` | Lighting at time of accident | Darkness KPI, severity heatmap |
| `Road_surface_conditions` | Surface condition (dry, wet, etc.) | Road risk dashboard |
| `Type_of_collision` | Collision type (rear-end, head-on, etc.) | Severity impact analysis |
| `Number_of_casualties` | Count of people injured or killed | Core KPI, statistical analysis |
| `severity_score` | Derived: slight=1, serious=2, fatal=3 | Numeric KPI computation |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| Severity Distribution % | Share of accidents by severity level | `count(severity) / total_accidents × 100` — Notebook 04, Section 14 |
| Mean Casualties per Accident | Average number of people hurt per accident | `mean(Number_of_casualties)` — Notebook 04, Section 15 |
| Fatal Injury Rate % | Percentage of accidents resulting in fatality | `count(fatal injury) / total × 100` — Notebook 04, Section 16 |
| Darkness Accident Rate % | Percentage of accidents occurring in darkness | `count(darkness conditions) / total × 100` — Notebook 04, Section 17 |
| Weekend Risk Index | Ratio of serious+fatal accidents on weekends vs weekdays | `is_weekend` flag — Notebook 05 |
| Severity Score | Numeric encoding of severity for aggregation | `slight=1, serious=2, fatal=3` — ETL pipeline + Notebook 05 |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Full Dashboard URL** | [View on Tableau Public](https://public.tableau.com/app/profile/arya.pandey1785/viz/FINALDVA/DVAProject?publish=yes) |
| **Dashboard 1 — Accident Severity Analysis** | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard1) |
| **Dashboard 2 — Driver Profile & Risk** | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard2) |
| **Dashboard 3 — Accident Risk & Severity** | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard3) |
| **Dashboard 4 — Time & Location Analysis** | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard4) |
| **Executive View** | High-level KPI summary — severity distribution, casualty counts, fatal rate, and top causes |
| **Operational View** | Drill-down by driver profile, time of day, road conditions, and collision type |
| **Main Filters** | Time Period, Day of Week, Area Type, Driver Age Band, Driving Experience, Weather |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

1. **Slight injuries dominate** — over 80% of accidents result in slight injuries, but serious and fatal cases cluster around specific, identifiable conditions.
2. **Inexperienced drivers (under 2 years) are the highest-risk group** — they appear disproportionately in serious and fatal accident records across all age bands.
3. **Young drivers aged 18–30 account for the largest share of accidents**, with severity compounded when combined with low driving experience.
4. **Evening hours (17:00–19:00) show the highest accident frequency**, aligning with peak traffic and driver fatigue patterns.
5. **Casualty counts are positively skewed** — the mean exceeds the median, meaning a small number of high-casualty incidents pull the average up significantly.
6. **Weekends show a higher proportion of serious and fatal injuries** compared to weekdays, suggesting different risk behavior outside commute hours.
7. **Darkness conditions are associated with higher severity outcomes** — accidents in unlit or poorly lit conditions trend toward serious and fatal categories.
8. **Overtaking and no distancing are the leading causes of accidents**, pointing to behavioral enforcement as the highest-leverage intervention.
9. **T-junctions and Y-junctions concentrate a disproportionate share of collisions**, indicating infrastructure-level risk hotspots.
10. **Normal weather accounts for the majority of accidents**, disproving the assumption that adverse weather is the primary risk driver — human behavior dominates.
11. **Road surface conditions show limited independent effect on severity** when controlling for driver behavior and time of day.
12. **Automobiles and heavy vehicles are involved in the most accidents**, with lorries skewing toward higher severity outcomes.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Inexperienced drivers are highest-risk | Mandate graduated licensing with night and highway restrictions for drivers under 2 years experience | Estimated 15–20% reduction in serious injuries among new drivers |
| 2 | Evening hours peak in accidents | Increase traffic enforcement and signal optimization during evening rush hours | Reduce peak-hour accident frequency by 10–15% |
| 3 | Overtaking and no distancing are top causes | Launch targeted behavioral campaigns and install speed/distance monitoring on high-risk corridors | Address the root cause of ~30% of recorded accidents |
| 4 | T-junctions and Y-junctions are collision hotspots | Prioritize junction redesign, better signage, and rumble strips at identified high-risk junctions | Reduce junction-related collisions by up to 25% |
| 5 | Darkness conditions increase severity | Accelerate street lighting upgrades on roads with high night-time accident rates | Lower fatal injury rate in darkness-related accidents by 10–20% |

---

## Repository Structure

```text
SectionA_Group7_RoadAccidents/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_EDA.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- project_report.pdf
|   `-- presentation.pdf
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline

1. **Define** — Sector selected (Public Safety), problem statement scoped, mentor approval obtained.
2. **Extract** — Raw RTA dataset sourced and committed to `data/raw/`; data dictionary drafted in `docs/`.
3. **Clean and Transform** — Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and `scripts/etl_pipeline.py`; processed output saved to `data/processed/`.
4. **Analyze** — EDA in `notebooks/03_EDA.ipynb`; full statistical analysis in `notebooks/04_statistical_analysis.ipynb`.
5. **Visualize** — Four interactive Tableau dashboards built and published on Tableau Public.
6. **Recommend** — Five data-backed business recommendations targeting driver behavior, infrastructure, and enforcement.
7. **Report** — Final project report and presentation exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |

**Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

---

## Submission Checklist

**GitHub Repository**
- [x] Public repository with correct naming convention
- [x] All notebooks committed in `.ipynb` format
- [x] `data/raw/` contains the original, unedited dataset
- [x] `data/processed/` contains the cleaned pipeline output
- [x] `tableau/screenshots/` contains dashboard screenshots
- [x] `tableau/dashboard_links.md` contains the Tableau Public URL
- [x] `docs/data_dictionary.md` is complete
- [x] `README.md` explains the project, dataset, and team

**Tableau Dashboard**
- [x] Published on Tableau Public and accessible via public URL
- [x] Interactive filters included
- [x] Dashboard directly addresses the business problem

**Project Report**
- [x] Final report exported as PDF into `reports/`
- [x] Final presentation exported as PDF into `reports/`

**Individual Assets**
- [x] DVA-oriented resumes added to `DVA-oriented-Resume/`
- [x] Portfolio links added to `DVA-focused-Portfolio/`

---

---

## Individual Contributions

---

### Keshav Rajput
#### Data Lead — Statistical Analysis & Report Writing

Conducted the full statistical analysis of the cleaned road accident dataset and contributed to the final project report. Responsible for building `04_statistical_analysis.ipynb` — the core analytical notebook of the project — and for adding the raw dataset that forms the foundation of all analysis.

#### Covers
- Set up the initial project structure and added the raw dataset to the repository
- Built `04_statistical_analysis.ipynb` (12,295 rows × 22 columns) covering:
  - **Univariate analysis** — mean, median, mode, variance, standard deviation, min, max, range
  - **Quartile & IQR analysis** — spread and outlier detection for numerical features
  - **Skewness analysis** — distribution shape assessment for all numerical columns
  - **Bivariate analysis** — casualties aggregated by accident severity, driving experience, and weather conditions
  - **Time-based analysis** — average casualties visualized across hours of the day
  - **Severity distribution** — count and percentage breakdown of slight / serious / fatal injuries
  - **KPI computation** — overall mean casualties, percentage of fatal injuries, percentage of accidents in darkness
  - **Distribution visualizations** — histograms and box plots for all numerical columns
- Authored the **Key Statistical Findings & Implications** section summarizing actionable insights
- Contributed to the **final project report** — writing, structuring, and documenting findings

#### Key Insight
Casualty counts are positively skewed, with the mean exceeding the median — indicating a small number of high-casualty accidents pulling the average up. Fatal injuries, though a minority, cluster around specific behavioral and temporal patterns, confirming that targeted interventions at peak hours and for inexperienced drivers can have the highest impact on reducing severity.

🌐 [DVA Portfolio](https://dva-portfolio-sand.vercel.app/)

---

### Hardik Maheshwari
#### Analysis Lead — EDA & Statistical Analysis

Led the analytical phase of the project by conducting in-depth Exploratory Data Analysis (EDA), statistical evaluation, and KPI computation using Python.

#### Covers
- Performed comprehensive **Exploratory Data Analysis (EDA)** on the cleaned dataset *(Notebook 03)*
- Conducted **statistical analysis and pattern validation** *(Notebook 04)*
- Analyzed relationships between features and accident severity using **univariate and bivariate techniques**
- Computed key **KPIs and risk indicators** for decision-making
- Identified **temporal, behavioral, and environmental patterns** influencing accident severity
- Generated insights to support **dashboard design and final reporting**

#### Key Insight
Accident severity is driven more by **behavioral factors (driver actions, experience, and timing)** than environmental conditions, with clear risk spikes during **evening hours and weekends**, and higher severity associated with specific driver and collision patterns.

🌐 [DVA Portfolio](https://hardikgenone.github.io/dva-portfolio/)

---

### Arya Pandey
#### Visualization Lead — Dashboard Design & Integration

Led the design and development of interactive Tableau dashboards, focusing on transforming processed data into clear, analytical visualizations. Played a key role in structuring dashboards, refining chart selection, and ensuring consistency across all visual outputs.

#### Covers
- Designed and developed the **Severity Overview Dashboard**
- Built the **Time & Pattern Analysis Dashboard**
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

#### Key Insight
Accident patterns are highly time-dependent, with clear peaks during rush hours and consistent high-risk time windows. Combining temporal trends with environmental and severity analysis shows that accidents follow predictable patterns influenced by human behavior and traffic conditions.

🌐 [DVA Portfolio](https://arya-p-gh.github.io/DVA_PORTFOLIO/)

---

### Suhaani Garg
#### Project Lead — Data Preparation, Dashboard Development & Report

Contributed across multiple stages of the project including data preprocessing, dashboard development, and reporting. Played a key role in refining datasets, improving dashboard quality, and ensuring consistency in the final analysis.

#### Covers
- Assisted in data cleaning and preprocessing using Google Colab (Python)
- Contributed to final dataset preparation and load pipeline in Python (`05_final_load_prep.ipynb`)
- Designed and developed **Dashboard 4** in Tableau
- Improved dashboard structure, layout, and interactivity
- Ensured data accuracy and consistency across visualizations
- Assisted in final project report and documentation

#### Key Insight
Accurate data preprocessing combined with well-structured dashboards improves the clarity, reliability, and interpretability of accident analysis, enabling better understanding of risk patterns and contributing factors.

🌐 [DVA Portfolio](https://suhaani-19.github.io/Data_Analytics_Portfolio/)

---

### Sathvik Koriginja
#### ETL Lead — Data Cleaning & Dashboard Development

Handled data preparation and visualization for the project. Cleaned, transformed, and structured raw accident data to ensure accuracy and usability for analysis, and built an interactive Tableau dashboard to present key insights.

#### Covers
- Data extraction and preprocessing
- Handling missing values and inconsistencies
- Feature engineering for analysis
- Preparing final dataset for visualization
- Building **Accident Risk & Severity Dashboard** in Tableau

#### Key Insight
Clean and well-structured data enabled accurate identification of accident patterns, highlighting that road conditions, vehicle movement, and collision types play a major role in severity outcomes.

🌐 [DVA Portfolio](https://sathvik89.github.io/DVA_Portfollio/)

---

### Krishna Dave
#### Strategy Lead — Driver Risk Analysis

Built an interactive Tableau dashboard analyzing how driver demographics affect road accident severity.

#### Covers
- Age vs Severity
- Driving Experience vs Severity
- Gender vs Severity
- Age × Experience Heatmap
- Weekend vs Weekday Risk

#### Key Insight
Inexperienced and young drivers form the highest-risk segment across all severity levels.

🌐 [DVA Portfolio](https://krishna-dave206.github.io/DVAPortfolio/)

---

### Anushka Tyagi
#### PPT & Quality Lead — Dashboard Analysis & Presentation

Designed interactive Tableau dashboards to analyze accident severity, driver risk, and overall incident patterns, and presented the insights through a PPT.

#### Covers
- Accident Severity Analysis
- Driver Profile & Risk Patterns
- Accident Risk & Contributing Factors
- Severity distribution across different conditions

#### Key Insight
Accident severity and risk are heavily influenced by driver profiles and external conditions, with clear patterns across different scenarios.

🌐 [DVA Portfolio](https://anu-ushka.github.io/DataAnalytics_Portfolio/)

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between stated contributions and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology — Data Visualization & Analytics | Capstone 2*
