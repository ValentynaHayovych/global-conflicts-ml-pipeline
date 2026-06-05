
==================================================================
# Global Conflicts ML Pipeline
==================================================================

Welcome to the **Global Conflicts ML Pipeline** repository!

This project analyzes a synthetic dataset of global conflicts.
It includes data validation and filtering (e.g., fact checking and coordinate validation), followed by anomaly detection using machine learning models such as Isolation Forest, Local Outlier Factor (LOF), Density-Based Spatial Clustering of Applications with Noise (DBSCAN).

The project also features data visualizations for comparison, an interactive map built with Folium, and a final validation summary matrix.


## Business Context
Organizations working with conflict and geopolitical data need to assess data quality before drawing conclusions.
This pipeline addresses three key questions:
- How reliable is the dataset across different validation checks?
- Which checks are statistically anomalous across key metrics such as death, GDP, coordinates?
- Which countries appear more frequently in conflicts and how do their records hold up to quality checks?


## Setup & Usage
1. Clone the repository
2. Create virtual environment: `python -m venv .venv`
3. Activate virtual environment: .venv\Scripts\activate
3. Install dependencies: `pip install -r requirements.txt`
4. Run the pipeline: `python main.py`


## Project structure:
```
│   .gitignore                                  # Files and directories to be ignored by Git
│   LICENSE                                     # License information for the repository
│   main.py                                     # The main entry point of the project. Runs the full ML pipeline: 
│                                                 -> data_loading -> data_validation -> ml_models -> ml_models_visuals -> overall_analysis
│   README.md                                   # Project overview and instructions
│   requirements.txt                            # Dependencies and requirements for the project
│   
├───config/                                     ## Config files
│   └───country_metrics.py                      # Structured country-level features covering independence year, population, GDP and geographical bounds
│           
├───data/                                       # Datasets
│   ├───processed/                              # Processed data with added data_validation and ml_models columns
│   └───raw/                                    # Raw dataset used in pipeline
│       └───global_conflicts_dataset.csv        # Raw synthetic dataset
│
├───output/
│   ├───analysis/                               # Visualized final evaluation with barcharts and matrices
│   ├───maps/                                   # Interactive html map with DBSCAN anomaly points
│   └───ml/                                     # ML models comparison visualizations
│
└───src/                                                      # Code
    ├───data_loading/                                         # Ingestion scripts
    │   └───load_data.py                                      # Data loading
    │           
    ├───data_validation/                                      # Fact checks and filtering based on coordinates
    │   │   _00_validate.py                                   # Runner
    │   │   _01_validation_conflict_type.py                   # Fact checks on conflict types
    │   │   _02_validation_year.py                            # Year validation based on countries' independence years provided in config file
    │   │   _03_validation_population.py                      # Population validation based on countries' current population provided in config file
    │   │   _04_validation_gdp.py                             # Population validation based on countries' current population provided in config file
    │   │   _05_validation_conflict_coordinates.py            # Coordinates validation based on countries' bounds provided in config file
    │   └───_06_conflict_coordinates_land_only.py             # Filter applied to the dataset to cut off offshore zone
    │     
    ├───ml_models/                                            # Anomaly detection models + clustering
    │   │   _00_ml_runner.py                                  # Runner
    │   │   _01_ml_iso_population_analysis.py                 # ML model Isolation Forest applied to analyse population
    │   │   _02_ml_iso_gdp_analysis.py                        # ML model Isolation Forest applied to analyse GDP
    │   │   _03_ml_lof_gdp_analysis.py                        # ML model Local Outlier Factor applied to analyse GDP
    │   │   _04_ml_iso_coordinates_analysis.py                # ML model Isolation Forest applied to analyse coordinates
    │   └───_05_ml_dbscan_deaths_coordinates_analysis.py      # ML model DBSCAN applied to analyse coordinates and mortality
    │           
    ├───ml_models_visuals/                                    # ML models visual comparison, including maps
    │   │   _00_plots_runner.py                               # Runner
    │   │   _01_plots_iso_gdp_anomalies.py                    # Isolation Forest GDP and GDP Loss Ratio dependencies visualizations
    │   │   _02_plots_iso_lof_gdp_anomalies.py                # Local Outlier Factor GDP and GDP Loss Ratio dependencies visualizations
    │   │   _03_plots_dbscan_iso_coordinates_anomalies.py     # Comparison of DBSCAN vs Isolation Forest outliers 
    │   │   _04_plots_dbscan_mortality_clustering.py          # Visualization of DBSCAN clustering results
    │   └───_05_plots_dbscan_interactive_map.py               # Interactive folium map with DBSCAN analysis results
    │                     
    ├───overall_analysis                                      # Final evaluation 
    │   │   _00_analysis.py                                   # Runner
    │   │   _01_a_plots_war_initiator_won.py                  # Rank of countries that initiated conflict and won - raw and filtered data
    │   │   _02_a_plots_war_defendor_lost.py                  # Rank of countries that were defenders and lost - raw and filtered data
    │   │   _03_a_plots_war_involvement_dbscan.py             # Total war involvment - raw and filtered data
    │   │   _04_a_final_data_validation.py                    # Matrix of all the data_validation results
    │   └───_05_a_final_ml_data_validation.py                 # Matrix of all the ml_models results
    │           
    └───prediction_models
        │   _00_prediction_models_evaluation.py               # Runner
        │   _01_logistic_regression.py                        # Logistic Regression pipeline
        └───_02_random_forest.py                              # Random Forest pipeline
```


## Key Findings:

### Data Quality Validation (Synthetic Dataset)
- Year validation passed for 81.3% of records = synthetic years are realistic.
- GDP and conflict coordinates validation failed for most records - synthetic values don't match real-world country data.
- Land-based coordinate filter retained 36% of records.
- Conflict type validation based on fact checks failed drastically with only 1.5% of valid data.

### Anomaly Detection Results
- *output/ml/plots_dbscan_iso_coordinates_anomalies.png*: location patterns anomalies with DBSCAN and ISO. 
DBSCAN marks anything geographically isolated as outlier taking local density as analysis basics, while Isolation Forest is more picky taking points that are statistically unusual compared to others, considering global distribution.
- *output/ml/plots_iso_gdp_anomalies.png*: left plot confirms synthetic GDP data is perfectly correlated between countries A and B. Right plot shows Isolation Forest successfully identifies anomalies based on global rarity, highlighting extreme GDP loss ratios and unusual economic impacts.
- *output/ml/plots_iso_lof_gdp_anomalies.png*: LOF detects anomalies based on local density deviations rather than global patterns - 
detecting points that are isolated relative to their immediate neighbourhood. As a result, LOF may miss
globally extreme values, while Isolation Forest which consistently captures those extremes.
- *output/ml/mortality_clustering_dbscan_bar.png*: DBSCAN effectively separates dense regions from sparsely distributed points,
and the large number of detected outliers (112) reflects true structural properties of the dataset rather than model
misconfiguration.
- *output/ml/dbscan_clusters_map.html*: interactive Folium map enriched with DBSCAN-based noise filtering selected as the most stable and interpretable anomaly-detection approach for the synthetic dataset provided.

### Prediction Models Training and Evaluation
- *src/prediction_models/*: Models Logistic Regression and Random Forest were trained and evaluated on synthetic data. The models showed limited predictive capability between features and target, with performance remaining close to random chance (~50% accuracy) under the current feature representation.

### Overall analysis
- Synthetic data quality is highly sensitive to rule-based validations *(output/analysis/final_data_validation.png)* which flag most records as invalid. For this reason, only land_only_coordinates_valid filtering was applied to the dataset *(src/data_validation/_06_conflict_coordinates_land_only.py)* before passing it to ML analysis.
- Among countries listed, USA, China and Russia show the highest pass rates across rule-based validations *(output/analysis/final_data_validation.png)*.
- ML-based anomaly detection identifies patterns based on feature rather than rule constraints *(output/analysis/final_ml_data_validation.png)*.

-> As an example, ML matrix *(output/analysis/final_ml_data_validation.png)* gave Ukraine the highest validation score and raw dataset contains over 400 records of its conflict involvement *(output/analysis/total_war_involvment.png)*, while after applying year, population and coordinates validations it has only 35 valid records *(output/analysis/total_war_involvment.png)*, making ML validation score that is based on raw data with land_only_coordinates filtering not reliable.

- Additional analyses of initiator victories *(output/analysis/war_initiator_wins.png)* and defender losses *(output/analysis/war_defender_lost.png)* reveal distributions that diverge substantially from overall war involvement *(output/analysis/total_war_involvment.png)*, after year validation, population validation and DBSCAN filtering, indicating that subgroup-specific dynamics become more pronounced once noisy or weakly-supported observations are removed.