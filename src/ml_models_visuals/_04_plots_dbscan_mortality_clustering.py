import matplotlib.pyplot as plt

def mortality_clustering_dbscan(adf):

    """
    Returns:
    - mortality_clustering_dbscan_bar.png
    """

    top_clusters = adf.groupby('DBSCAN_Cluster')['DBSCAN_Cluster'].size().sort_values(ascending=False)
    colors = ['purple' if x == -1 else 'green' for x in top_clusters.index]

    fig = plt.figure(figsize=(12,5))
    plt.bar(top_clusters.index, top_clusters.values, color=colors)
    plt.title('DBSCAN Clusters of Mortality Anomalies (Top20)')
    plt.xlabel('Cluster Label')
    plt.ylabel('Number of Records')

    plt.tight_layout()

    return fig


