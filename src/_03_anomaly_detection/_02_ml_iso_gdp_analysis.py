from sklearn.ensemble import IsolationForest

def iso_gdp_analysis(df):
    
    """
    Analyses GDP columns using Isolation Forest.
    Returns:
        - GDP_Loss_Ratio: share of economic loss to total GDP.
        - GDP_IF_Label: Isolation Forest label for GDP values.
        - GDP_Loss_IF_Label: Isolation Forest label for GDP loss ratio values.
        - GDP_IF_Valid: Binary indicator of whether GDP values are valid (1) or anomalous (0).
        - GDP_Loss_IF_Valid: Binary indicator of whether GDP loss ratio values are valid
    """

    iso = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
    
    # GDP Loss Ratio
    df['GDP_Loss_Ratio'] = df['Economic_Loss_USD_Billions'] / (df['GDP_A_Billions'] + df['GDP_B_Billions'])

    df['GDP_IF_Label'] = iso.fit_predict(df[['GDP_A_Billions', 'GDP_B_Billions']])
    df['GDP_Loss_IF_Label'] = iso.fit_predict(df[['GDP_Loss_Ratio', 'Economic_Loss_USD_Billions']])

    df['GDP_IF_Valid'] = (df['GDP_IF_Label'] == 1).astype(int)
    df['GDP_Loss_IF_Valid'] = (df['GDP_IF_Label'] == 1).astype(int)

    return df