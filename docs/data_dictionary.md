# Data Dictionary

---

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Road Traffic Accident (RTA) Dataset |
| Source | Kaggle / Government Road Safety Data |
| Raw file name | RTA Dataset.csv |
| Cleaned file name | CLEANED Dataset.csv |
| Raw dataset size | 12,316 rows × 32 columns |
| Cleaned dataset size | 12,295 rows × 22 columns |
| Last updated | April 2026 |
| Granularity | One row per accident |

---

## Data Cleaning Summary

- **Rows removed:** 21  
  - Removed due to missing or inconsistent critical values (e.g., accident severity, time, driver details)

- **Columns removed:**  
  - Age_band_of_casualty  
  - Casualty_class  
  - Casualty_severity  
  - Defect_of_vehicle  
  - Educational_level  
  - Fitness_of_casuality  
  - Number_of_vehicles_involved  
  - Owner_of_vehicle  
  - Pedestrian_movement  
  - Road_surface_type  
  - Service_year_of_vehicle  
  - Sex_of_casualty  
  - Vehicle_driver_relation  
  - Work_of_casuality  

### Why columns were removed:
- High percentage of missing values (30–40%+)  
- Low relevance to key analysis (severity, driver behavior, road conditions)  
- Redundant or weak contribution to KPIs  
- Would introduce noise in visualization and reduce model reliability  

| Column Name                     | Justification                                                                 |
|--------------------------------|------------------------------------------------------------------------------|
| Educational_level              | Limited direct impact on actionable decision-making for accident prevention  |
| Vehicle_driver_relation        | Does not influence infrastructure or policy-level decisions                  |
| Owner_of_vehicle               | Minimal relevance to accident patterns or severity outcomes                 |
| Service_year_of_vehicle        | Low impact compared to more critical safety factors                         |
| Defect_of_vehicle              | Inconsistent and unreliable for high-level analysis                         |
| Road_surface_type              | Less informative than Road_surface_conditions                               |
| Number_of_vehicles_involved    | Redundant with collision type and casualty count                            |
| Casualty_class                 | Focus is on accident-level, not individual roles                            |
| Sex_of_casualty                | Low relevance for policy or infrastructure decisions                        |
| Age_band_of_casualty           | Limited contribution to reducing accident occurrence                        |
| Casualty_severity              | Redundant with Accident_severity                                            |
| Work_of_casuality              | Not useful for actionable road safety insights                              |
| Fitness_of_casuality           | Inconsistent and not relevant for macro-level decisions                     |
| Pedestrian_movement            | Too granular for overall dashboard insights                                 |


---

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| Accident_severity | string | Severity level of accident | slight injury | KPI, Tableau | Lowercased, mapped to severity_score |
| Number_of_casualties | int | Number of people injured/killed | 3 | KPI, charts | Converted to numeric, removed negatives |
| Time | datetime | Time of accident | 14:30:00 | Time analysis | Converted to datetime |
| Day_of_week | string | Day of accident | monday | Weekend KPI | Lowercased, standardized |
| Area_accident_occured | string | Area type where accident occurred | urban area | Filters | Removed invalid merged value |
| Types_of_Junction | string | Type of road junction | t-junction | Intersection analysis | Standardized |
| Road_allignment | string | Road structure/shape | straight road | Risk dashboard | Standardized |
| Lanes_or_Medians | string | Road lane configuration | two-way | Optional analysis | Standardized |
| Weather_conditions | string | Weather during accident | raining | Heatmap | Standardized |
| Light_conditions | string | Lighting condition | daylight | Severity analysis | Standardized |
| Road_surface_conditions | string | Road surface condition | dry | Risk charts | Standardized |
| Type_of_collision | string | Type of collision | vehicle collision | Severity impact | Standardized |
| Vehicle_movement | string | Movement of vehicle | going straight | KPI | Standardized |
| Cause_of_accident | string | Main cause of accident | no distancing | Cause chart | Standardized |
| Age_band_of_driver | string | Driver age group | 18-30 | Risk analysis | Standardized |
| Driving_experience | string | Experience level of driver | 2-5yr | Severity impact | Standardized |
| Sex_of_driver | string | Gender of driver | male | Gender analysis | Standardized |
| Type_of_vehicle | string | Type/category of vehicle | car | Severity index | Standardized |

---

## Derived Columns

| Derived Column | Logic | Business Meaning |
|---|---|---|
| Hour | Time.dt.hour | Extracts hour for time-based analysis |
| Time_period | Night (0-6), Morning (6-12), Afternoon (12-18), Evening (18-24) | Identifies high-risk time slots |
| severity_score | slight=1, serious=2, fatal=3 | Converts severity into numeric KPI |
| is_weekend | Day_of_week in (saturday, sunday) | Helps compare weekday vs weekend risk |

---

## Data Quality Notes

- Dataset reduced from **12,316 to 12,295 rows** with minimal data loss  
- Columns reduced from **32 to 22**, improving focus and usability  
- Missing values handled using:
  - Mode for categorical columns  
  - Median for numerical columns  
- High-null columns were removed to ensure reliability  
- All categorical values standardized (lowercase, trimmed, cleaned)  
- Removed duplicate records  
- Removed invalid entry: **"rural village areasoffice areas"**  
- Time conversion introduced minor nulls, which were handled  
- Dataset is **imbalanced** (majority cases = slight injury)  
- Feature engineering applied for better trend and KPI analysis  

---
