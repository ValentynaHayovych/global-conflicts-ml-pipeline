from src._01_data_loading.load_data import load_data
from src._02_data_validation._00_validate import data_validation
from src._03_anomaly_detection._00_ml_runner import anomaly_detection
from src._04_classification._00_prediction_models_evaluation import evaluate_prediction_models
from src._05_visualization._00_plots_runner import ml_visualizations
from src._06_analysis._00_analysis import final_analysis



def main():
    print("=" * 60)
    print('=== Global Conflicts ML Pipeline ==='.center(60))
    print("=" * 60)

    df = load_data('data/raw/global_conflicts_dataset.csv')
    print('[INFO] Dataset loaded.')
    print(f"Dataset contains {len(df)} rows.\n")

    vdf = data_validation(df)
    print('[INFO] Dataset validation completed.')

    adf = anomaly_detection(vdf)
    print('\n[INFO] Anomaly detection completed.\n')

    evaluate_prediction_models(adf)
    print('[INFO] Prediction models trained and evaluated.\n')

    adf.to_csv('data/processed/global_conflicts_anomalies.csv', index=False)
    print('[INFO] Processed dataset saved.')

    ml_visualizations(adf) 
    print('[INFO] Visualizations generated and saved to: outputs/.')

    final_analysis(df, adf)
    print('[INFO] Analysis complete.')

    print("=" * 60)
    print('Pipeline completed successfully.'.center(60))
    print("=" * 60)
    
    
if __name__ == "__main__":
    main()