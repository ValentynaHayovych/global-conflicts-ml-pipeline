from sklearn.neighbors import LocalOutlierFactor

def gdp_lof_analysis(df):
    
    """
    Analyses GDP columns using LOF.
    Returns:
        - GDP_LOF_Label: LOF label for GDP values.
        - GDP_Loss_LOF_Label: LOF label for GDP loss ratio values.
        - GDP_LOF_Valid: Binary indicator of whether GDP values are valid (1) or anomalous (0).
        - GDP_Loss_LOF_Valid: Binary indicator of whether GDP loss ratio values are valid
    """
     
    lof = LocalOutlierFactor(n_neighbors=20, contamination=0.03)

    df['GDP_LOF_Label'] = lof.fit_predict(df[['GDP_A_Billions', 'GDP_B_Billions']])
    df['GDP_Loss_LOF_Label'] = lof.fit_predict(df[['GDP_Loss_Ratio', 'Economic_Loss_USD_Billions']])
    
    df['GDP_LOF_Valid'] = (df['GDP_LOF_Label'] == 1).astype(int)
    df['GDP_Loss_LOF_Valid'] = (df['GDP_Loss_LOF_Label'] == 1).astype(int)

    return df
