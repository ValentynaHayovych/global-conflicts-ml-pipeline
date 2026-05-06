from src.ml_models_visuals._01_plots_iso_gdp_anomalies import gdp_anomalies_iso
from src.ml_models_visuals._02_plots_iso_lof_gdp_anomalies import gdp_anomalies_lof
from src.ml_models_visuals._03_plots_dbscan_iso_coordinates_anomalies import coordinates_anomalies_dbscan_iso
from src.ml_models_visuals._04_plots_dbscan_mortality_clustering import mortality_clustering_dbscan
from src.ml_models_visuals._05_plots_dbscan_interactive_map import interactive_dbscan_map
import matplotlib.pyplot as plt

def visualizations(adf):

    plots = {
        'plots_iso_gdp_anomalies': gdp_anomalies_iso(adf),
        'plots_iso_lof_gdp_anomalies': gdp_anomalies_lof(adf),
        'plots_dbscan_iso_coordinates_anomalies': coordinates_anomalies_dbscan_iso(adf),
        'mortality_clustering_dbscan_bar': mortality_clustering_dbscan(adf)
    }
    
    for name, fig in plots.items():
        fig.savefig(f'output/ml/{name}', dpi=300)
        plt.close(fig)

    fmap = interactive_dbscan_map(adf)
    fmap.save('output/maps/dbscan_clusters_map.html')
  