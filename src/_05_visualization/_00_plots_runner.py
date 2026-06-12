from src._05_visualization._01_plots_iso_gdp_anomalies import gdp_anomalies_iso
from src._05_visualization._02_plots_lof_gdp_anomalies import gdp_anomalies_lof
from src._05_visualization._03_plots_dbscan_iso_coordinates_anomalies import coordinates_anomalies_dbscan_iso
from src._05_visualization._04_conflict_coordinates_dbscan_statistics import conflict_coordinates_dbscan_clustering_statistics
from src._05_visualization._05_plots_dbscan_interactive_map import interactive_dbscan_map
import matplotlib.pyplot as plt

def ml_visualizations(adf):

    plots = {
        'plots_iso_gdp_anomalies': gdp_anomalies_iso(adf),
        'plots_lof_gdp_anomalies': gdp_anomalies_lof(adf),
        'plots_dbscan_iso_coordinates_anomalies': coordinates_anomalies_dbscan_iso(adf),
        'dbscan_coordinates_clustering_statistics': conflict_coordinates_dbscan_clustering_statistics(adf)
    }
    
    for name, fig in plots.items():
        fig.savefig(f'output/ml/{name}', dpi=300)
        plt.close(fig)

    fmap = interactive_dbscan_map(adf)
    fmap.save('output/maps/dbscan_clusters_map.html')
  