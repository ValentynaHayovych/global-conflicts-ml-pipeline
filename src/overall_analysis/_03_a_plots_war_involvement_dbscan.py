import matplotlib.pyplot as plt

def war_involvement(df, adf):

    """
    Function creates barcharts of countries total war involvment 
    with visual comparison between raw and filtered dataset, 
    included also Year_Valid and Population_Valid validations as filters.
    Returns:
    - total_war_involvment.png
    """
    # Total war involvement per country
    war_involvement = (
        df[['Country_A', 'Country_B']]
        .melt(value_name='Country')
        .groupby('Country')
        .size()
        .reset_index(name='War_Involvement')
        .sort_values(by='War_Involvement', ascending=False)
    )

    # Total war involvment per country that are labeled as Anomalies by DBSCAN
    yeva = adf[adf['Year_Valid'] == 1] # added year filtering 
    pova = yeva[yeva['Population_Valid'] == 1] # added population filtering
    ano = pova[pova['DBSCAN_Cluster'] != -1]
    dbscan_anomalies = (
        ano[['Country_A', 'Country_B']]
        .melt(value_name='Country')
        .groupby('Country')
        .size()
        .reset_index(name='DBSCAN_Anomalies')
        .sort_values(by='DBSCAN_Anomalies', ascending=False)
    )

    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    cmap = plt.get_cmap('YlGnBu')

    axes[0].bar(war_involvement['Country'], war_involvement['War_Involvement'], color = cmap(0.55))
    axes[0].set_title('Total war involvement per country')
    axes[0].tick_params(axis = 'x', rotation=45)

    axes[1].bar(dbscan_anomalies['Country'], dbscan_anomalies['DBSCAN_Anomalies'], color = cmap(0.6))
    axes[1].set_title('Total approved war involvement (DBSCAN)')
    axes[1].tick_params(axis = 'x', rotation=45)

    plt.tight_layout()
    return fig

