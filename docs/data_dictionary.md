# Data Dictionary

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | Road Traffic Accident (RTA) Dataset |
| Source | Kaggle / Government Road Safety Data |
| Raw file name | RTA Dataset.csv |
| Last updated | Not specified |
| Granularity | One row per accident |

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

- Missing values replaced using:
  - Mode for categorical columns
  - Median for numerical columns  
- Standardized inconsistent values (unknown, NA, - → null)  
- All text converted to lowercase and trimmed  
- Removed duplicate records  
- Removed invalid entry: "rural village areasoffice areas"  
- Time conversion caused minor nulls (handled)  
- Dataset is imbalanced (majority = slight injury)  