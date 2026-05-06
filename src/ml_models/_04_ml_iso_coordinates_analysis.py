from sklearn.ensemble import IsolationForest

def iso_coordinates_analysis(df):
    
    """
    Analyses coordinates using Isolation Forest.
    Returns:
        - Coords_IF_Valid: Binary indicator of whether coordinates are valid (1) or anomalous (0) based on latitude and longitude.
    """
    
    iso = IsolationForest(n_estimators = 100, contamination = 0.03, random_state = 42)

    coords = df[['Latitude', 'Longitude']]

    df['Coords_IF_Label'] = iso.fit_predict(coords)

    df['Coords_IF_Valid'] = (df['Coords_IF_Label'] == 1).astype(int)

    return df