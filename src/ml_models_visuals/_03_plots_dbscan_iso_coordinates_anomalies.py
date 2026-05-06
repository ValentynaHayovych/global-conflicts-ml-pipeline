import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets

def coordinates_anomalies_dbscan_iso(df):

    """
    Creates a side-by-side plots of global conflict coordinates anomalies 
    using DBSCAN clustering and Isolation Forest anomaly detection. 
    The left plot shows the DBSCAN clusters. 
    The right plot highlights the anomalies detected by Isolation Forest. 
    Both plots are overlaid on a world map for geographical context.
    Returns:
    - plots_dbscan_iso_coordinates_anomalies.png
    """

    # World map
    world = gpd.read_file(geodatasets.get_path('naturalearth.land'))

    # Subplots
    fig, axes = plt.subplots(1, 2, figsize=(14,5))

    # DBSCAN clusters
    world.plot(ax=axes[0], color = 'lightgrey', edgecolor='darkgrey')
    anomalies = df[df['Coords_DBSCAN_Valid'] == 0]
    normal = df[df['Coords_DBSCAN_Valid'] == 1]
    axes[0].scatter(normal['Longitude'], normal['Latitude'], 
                    c='yellow', s = 6, edgecolor = 'green')
    axes[0].scatter(anomalies['Longitude'], anomalies['Latitude'], 
                    c='purple', s = 7, edgecolor='#4B0082')
    axes[0].set_title('Coordinates Clusters - DBSCAN')
    axes[0].set_xlabel('Longitude')
    axes[0].set_ylabel('Latitude')

    # Isolation Forest
    world.plot(ax=axes[1], color='lightgrey', edgecolor='darkgrey')
    anomalies1 = df[df['Coords_IF_Valid'] == 0]
    normal1 = df[df['Coords_IF_Valid'] == 1]
    axes[1].scatter(normal1['Longitude'], normal1['Latitude'], 
                    c='yellow', s = 6, edgecolor = 'green')
    axes[1].scatter(anomalies1['Longitude'], anomalies1['Latitude'], 
                    c='purple',  s = 7, edgecolor='#4B0082')

    axes[1].set_title('Coordinates Anomalies - Isolation Forest')
    axes[1].set_xlabel('Longitude')
    axes[1].set_ylabel('Latitude')

    plt.tight_layout()

    return fig



