from src.data_loading.load_data import load_data
from src.data_validation._00_validate import validate_data
from src.ml_models._00_ml_runner import anomaly_results
from src.ml_models_visuals._00_plots_runner import visualizations
from src.overall_analysis._00_analysis import analysis


def main():
    print("=" * 60)
    print('=== Global Conflicts ML Pipeline ==='.center(60))
    print("=" * 60)

    df = load_data('data/raw/global_conflicts_dataset.csv')
    print('[INFO] Dataset loaded: data/raw/global_conflicts_dataset.csv.')
    print(f"Dataset contains {len(df)} rows.\n")

    vdf = validate_data(df)
    print('[INFO] Dataset validation completed.')

    adf = anomaly_results(vdf)
    print('\n[INFO] Anomaly detection completed (DBSCAN, LOF and Isolation Forest applied).')

    adf.to_csv('data/processed/global_conflicts_anomalies.csv', index=False)
    print('[INFO] Processed dataset saved: data/processed/global_conflicts_anomalies.csv.')

    visualizations(adf) 
    print('[INFO] Visualizations saved to: outputs/.')

    analysis(df, adf)
    print('[INFO] Analysis completed (initial, validated and anomaly-based).')

    print("=" * 60)
    print('Pipeline completed successfully.'.center(60))
    print("=" * 60)
    
    
if __name__ == "__main__":
    main()