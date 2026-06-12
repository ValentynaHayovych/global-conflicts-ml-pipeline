import matplotlib.pyplot as plt

def conflict_coordinates_dbscan_clustering_statistics(adf):

    """
    Returns:
    - conflict_coordinates_dbscan_statistics.png
    """

    top_clusters = adf.groupby('DBSCAN_Cluster')['DBSCAN_Cluster'].size().sort_values(ascending=False)
    colors = ['purple' if x == -1 else 'green' for x in top_clusters.index]

    fig = plt.figure(figsize=(12,5))
    plt.bar(top_clusters.index, top_clusters.values, color=colors)
    plt.title('Conflict Coordinates DBSCAN Clustering Statistics')
    plt.xlabel('Cluster Label')
    plt.ylabel('Number of Records')

    plt.tight_layout()

    return fig


