from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def dbscan_deaths_coordinates_analysis(df):

    """
    Analyses the relationship between total deaths and coordinates using DBSCAN.
    Returns:
        - DBSCAN_Cluster: Cluster labels assigned by DBSCAN.
        - Death_Coords_DBSCAN_Valid: binary indicator of whether coordinates are valid (1) or anomalous (0).
    """

    x = df[['Latitude', 'Longitude']]
    db = DBSCAN(eps=5, min_samples=3)
    df['DBSCAN_Cluster'] = db.fit_predict(x)
    df['Coords_DBSCAN_Valid'] = (df['DBSCAN_Cluster'] != -1).astype(int)

    scaler = StandardScaler()
    y = df[['Total_Deaths', 'Latitude', 'Longitude']]
    y_scaled = scaler.fit_transform(y)
    db_scaled = DBSCAN(eps=0.5, min_samples=3)
    df['Total_Deaths_DBSCAN_Cluster'] = db_scaled.fit_predict(y_scaled)
    df['Total_Deaths_DBSCAN_Valid'] = (df['Total_Deaths_DBSCAN_Cluster'] != -1).astype(int)

    return df
    
