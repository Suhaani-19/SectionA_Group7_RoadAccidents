# 🚦 Road Accident Severity Analysis — Section A, Group 7

A data analytics capstone project analyzing road traffic accident patterns, severity drivers, and risk factors using Python and Tableau.

---

## 📁 Project Structure

```
SectionA_Group7_RoadAccidents/
├── data/
│   ├── raw/                        # Original dataset (never modified)
│   │   └── RAW Dataset.csv
│   └── processed/                  # Cleaned, analysis-ready dataset
│       └── CLEANED Dataset.csv
├── notebooks/
│   ├── 01_extraction.ipynb         # Data extraction & initial inspection
│   ├── 02_cleaning.ipynb           # Data cleaning & preprocessing
│   ├── 03_EDA.ipynb                # Exploratory Data Analysis
│   ├── 04_statistical_analysis.ipynb  # Statistical analysis & KPIs
│   └── 05_final_load_prep.ipynb    # Final dataset preparation & load
├── scripts/
│   └── etl_pipeline.py             # Automated ETL pipeline (CLI)
├── tableau/
│   ├── dashboard_links.md          # Links to all Tableau dashboards
│   └── screenshots/
│       ├── charts/                 # Individual chart screenshots
│       └── dashboards/             # Full dashboard screenshots
├── reports/
│   ├── project_report.pdf          # Final project report
│   └── presentation.pdf            # Project presentation slides
├── docs/
│   └── data_dictionary.md          # Column definitions & data quality notes
├── DVA-oriented-Resume/            # DVA-focused resumes of team members
└── DVA-focused-Portfolio/          # DVA portfolio links of team members
```

---

## 📊 Dataset Overview

| Item | Details |
|---|---|
| Source | Road Traffic Accident (RTA) Dataset |
| Raw rows | ~12,316 |
| Cleaned rows | 12,295 |
| Columns | 22 (18 original + 4 derived) |
| Target variable | `Accident_severity` (slight / serious / fatal injury) |

---

## 🚀 Getting Started

### Prerequisites

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Run the ETL Pipeline

```bash
python scripts/etl_pipeline.py --input data/raw/"RAW Dataset.csv" --output data/processed/"CLEANED Dataset.csv"
```

### Run Notebooks

Open notebooks in order using Jupyter or Google Colab:

```bash
jupyter notebook
```

Run `01_extraction.ipynb` → `02_cleaning.ipynb` → `03_EDA.ipynb` → `04_statistical_analysis.ipynb` → `05_final_load_prep.ipynb`

---

## 📈 Tableau Dashboards

| Dashboard | Link |
|---|---|
| 🔗 Full Project Dashboard | [View on Tableau Public](https://public.tableau.com/app/profile/arya.pandey1785/viz/FINALDVA/DVAProject?publish=yes) |
| Dashboard 1 — Accident Severity Analysis | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard1) |
| Dashboard 2 — Driver Profile & Risk | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard2) |
| Dashboard 3 — Accident Risk & Severity | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard3) |
| Dashboard 4 — Time & Location Analysis | [View](https://public.tableau.com/app/profile/krishna.dave3250/viz/FINALDVA1/Dashboard4) |

---

## 👥 Team — Section A, Group 7

| Name | Role | Portfolio |
|---|---|---|
| Keshav Rajput | Statistical Analysis & Report Writing | [🌐 Portfolio](https://dva-portfolio-sand.vercel.app/) |
| Hardik Maheshwari | EDA & Statistical Analysis Lead | [🌐 Portfolio](https://hardikgenone.github.io/dva-portfolio/) |
| Arya Pandey | Visualization Design & Dashboard Integration | [🌐 Portfolio](https://arya-p-gh.github.io/DVA_PORTFOLIO/) |
| Suhaani Garg | Data Preparation, Dashboard Development & Report | [🌐 Portfolio](https://suhaani-19.github.io/Data_Analytics_Portfolio/) |
| Sathvik Koriginja | Data Cleaning & Dashboard Development | [🌐 Portfolio](https://sathvik89.github.io/DVA_Portfollio/) |
| Krishna Dave | Driver Risk Analysis & Dashboard | — |
| Anushka Tyagi | Dashboard Analysis & Presentation | [🌐 Portfolio](https://anu-ushka.github.io/DataAnalytics_Portfolio/) |

---

## 🤝 Contributions

---

### Keshav Rajput
#### Statistical Analysis & Report Writing

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
#### EDA & Statistical Analysis Lead

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
#### Visualization Design, Dashboard Development & Integration

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
#### Data Preparation, Dashboard Development & Report Contribution

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
#### Data Cleaning & Dashboard Development

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
#### Driver Risk Analysis

Built an interactive Tableau dashboard analyzing how driver demographics affect road accident severity.

#### Covers
- Age vs Severity
- Driving Experience vs Severity
- Gender vs Severity
- Age × Experience Heatmap
- Weekend vs Weekday Risk

#### Key Insight
Inexperienced and young drivers form the highest-risk segment across all severity levels.

---

### Anushka Tyagi
#### Road Accident Dashboard Analysis

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

## 📄 License

This project is for academic purposes as part of the DVA Capstone — Section A, Group 7.
