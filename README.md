
==================================================================
# Global Conflicts ML Pipeline
==================================================================

Welcome to the **Global Conflicts ML Pipeline** repository!

This project analyzes a synthetic dataset of global conflicts.
It includes data validation and filtering (e.g., fact checking and coordinate validation),followed by anomaly detection using machine learning models such as Isoation Forest, Local Outlier Factor (LOF), Density-Based Spatial Clustering of Applications with Noise (DBSCAN).

The project also features data visualizations for comparison, an interactive map built with Folium, and a final validation summary matrix.


## Project structure:

global-conflicts-ml-pipeline/

config/                            # Structured country-level features covering independence year, population, GDP and geographical bounds

data/                            
── processed/                      # Processed data with added data_validation and ml_models columns
── raw/                            # Raw synthetic dataset

output/                               
── analysis/                       # Visualized final evaluation with barcharts and matrixes
── maps/                           # Interactive html map with DBSCAN anomaly points
── ml/                             # ML models comparison visualisations

src/        
── data_loading/                   # Ingestion scripts                         
── data_validation/                # Fact checks and filtering based on coordinates          
── ml_models/                      # Clustering + anomaly detection models   
── ml_models_visuals/              # ML models visual comparison, including maps
── overall_analysis/               # final evaluation 

── main.py                         # The main entry point of the project. Runs the full ML pipeline: data_loading -> data_validation -> ml_models -> ml_models_visuals -> overall_analysis        
── README.md                       # Project overview and instructions   
── requirements.txt                # Dependencies and requirements for the project           
── LICENSE                         # License information for the repository   
── .gitignore                      # Files and directories to be ignored by Git 

## Key Findings:

**Data Quality Validation (Synthetic Dataset)**
- Year validation passed for 97.6% of records = synthetic years are realistic.
- GDP and conflict coordinates validation failed for most records - synthetic values don't match real-world country data.
- Land-based coordinate filter retained 36% of records.
- Conflict type validation based on fact checks failed drastically with only 1.5% of valid data.

**Anomaly Detection Results**
- *output/ml/plots_dbscan_iso_coordinates_anomalies*: location patterns anomalies with DBSCAN and ISO. 
DBSCAN marks anythiing geographically isolated as outlier taking local density as analysis basics, while Isolation Forest is more picky taking points that are statistically unusual compared to others, considering global distribution.
- *output/ml/plots_iso_gdp_anomalies*: left plot confirms syntheetic GDP data is perfectly correlated between countries A and B. Right plot shows Isolation Forest successfully identifies anomalies based on global rarity, highlighting extreme GDP loss ratios and unusual economic impacts.
- *output/ml/plots_iso_lof_gdp_anomalies*: LOF detects anomalies based on local density deviations rather than global patterns - 
detecting points that are isolated relative to their immediate neighbourhood. As a result, LOF may miss
globally extreme values, while Isoation Forest which consistently captures those extremes.
- *output/ml/mortality_clustering_dbscan_bar*: DBSCAN effectively separates dense regions from sparsely distributed points,
and the large number of detected outliers (112) reflects true structural properties of the dataset rather than model
misconfiguration.

**Overall analysis**
- Synthetic data quality is highly sensitive to rule-based validations *(output/analysis/final_data_validation.png)* which flag most records as invalid. For this reason, only land_only_coordinates_valid filtering was applied to the dataset *(src/data_validation/_06_conflict_coordinates_land_only.py)* before passing it to ML analysis.
- Among countries listed, USA, China and Russia show the highest pass rates across rule-based validations *(output/analysis/final_data_validation.png)*.
- ML-based anomaly detection identifies patterns based on feature rather than rule constrains *(output/analysis/final_ml_data_validation.png)*.

-> As an example, ML matrix *(output/analysis/final_ml_data_validation.png)* gave Ukraine the highest validation score and raw dataset contains over 400 records of its conflict involvment *(output/analysis/total_war_involvment.png)*, while after aplying year, population and coordinates validations it has only 35 valid records *(output/analysis/total_war_involvment.png)*, making ML validation score that is based on raw data with land_only_coordinates filtering not reliable.

- Additional breakdowns such as initiator wins *(output/analysis/war_initiator_wins.png)* and defender losses *(output/analysis/war_defender_lost.png)* show highly similar distributions to total war involvment *(output/analysis/total_war_involvment.png)*, suggesting limited additional information beyond the aggregate metric.



