# Global Conflicts ML Pipeline

Welcome to the **Global Conflicts ML Pipeline** repository!


## Project Overview

This project evaluates the reliability of geopolitical conflict data and demonstrates how poor data quality impacts downstream analytics and machine learning model results.
It combines rule-based validation, anomaly detection models, and geospatial analysis.
The project features data visualizations for comparison, an interactive map built with Folium, and a final validation summary matrix.


## Business Context

Organizations frequently begin analytics or machine learning work before fully establishing that their data is trustworthy, and data quality issues remain one of the most common causes of poor analytical outcomes.
A critical question to be answered:
**Can this dataset be trusted for analytical or predictive use?**


## Key Insight

> Most records in the dataset fail basic validation checks, and machine learning models applied to unvalidated data produce misleading results.

This project shows that **data validation is not optional — it fundamentally changes analytical conclusions.**


## Pipeline Architecture
```
Raw synthetic dataset

        ↓

DATA VALIDATION → Conflict Type → Year → Population → GDP → Conflict Coordinates

        ↓

ANOMALY DETECTION → Isolation Forest (ISO) · Local Outlier Factor (LOF) · DBSCAN

        ↓

PREDICTION MODELS → Logistic Regression · Random Forest

        ↓

ML VISUALIZATIONS → ISO & LOF GDP Comparison · ISO & DBSCAN Map Coordinates Labeling · DBSCAN Clusters Statistics

        ↓

FINAL EVALUATION → Raw & Validated Data Statistics Comparison · Validation Matrix · Machine Learning Matrix

```


## Tech Stack

Python 3.12 · Pandas · Scikit-learn · Folium · Matplotlib · Seaborn · Geopandas · Geodatasets


## Project structure:

[Project Structure Tree](project_structure_tree.txt)


## Project Flow

### 1. Data Validation Layer

Applies rule-based checks using external country-level benchmarks:

* Year vs country independence
* Population and GDP consistency
* Coordinate validation (including land-only filtering)

**Result:**
Data quality assessment reduced trusted records by 98.5%, exposing significant data quality issues and demonstrates that conclusions drawn from the raw dataset would have been based primarily on invalid observations.


### 2. Anomaly Detection Layer

Applies multiple models to detect unusual patterns:

* Isolation Forest (global anomalies)
* Local Outlier Factor (local density anomalies)
* DBSCAN (geospatial clustering)

**Observation:**
Different models identify different types of anomalies, highlighting the importance of model selection depending on context.


### 3. Geospatial Analysis

* Interactive map (Folium) visualizing DBSCAN clusters and outliers
* Identifies spatial inconsistencies and unrealistic conflict locations


### 4. Comparative Analysis

Compares:

* Raw dataset vs validated dataset
* Rule-based validation vs ML-based anomaly detection

**Key Finding:**
ML models trained on insufficiently validated data produce results that appear plausible but are statistically unreliable.


## Results

### Data Quality

* Year validation: ~81% pass rate
* Conflict type validation: ~1.5% pass rate
* Coordinate + GDP validation: majority fail
* Land-only filtering reduces dataset to ~36%

### Machine Learning

* Anomaly detection highlights structural inconsistencies in synthetic data
* Predictive models (Logistic Regression, Random Forest) perform no better than random chance (~50% accuracy), indicating insufficient signal for reliable forecasting


## Why This Matters

This project demonstrates a common failure in analytics workflows:

> Applying machine learning without validating data leads to false confidence and incorrect conclusions.

It provides a structured approach to:

* Assess dataset reliability
* Compare validation vs ML-based anomaly detection
* Understand when data is not suitable for predictive modeling


## Setup & Usage

1. Clone the repository
2. Create virtual environment inside the repository in terminal: `python -m venv .venv`
3. Activate virtual environment: .venv\Scripts\activate
4. Install dependencies: `pip install -r requirements.txt`
5. Run the pipeline: `python main.py`
