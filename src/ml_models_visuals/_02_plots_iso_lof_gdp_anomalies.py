import matplotlib.pyplot as plt

def gdp_anomalies_lof(df):

    """
    Creates a side-by-side plot of global conflict GDP anomalies using Local Outlier Factor (LOF) anomaly detection. 
    The left plot shows GDP anomalies based on GDP_A_Billions and GDP_A_Billions.
    The right plot shows GDP loss anomalies based on GDP_Loss_Ratio and Economic_Loss_USD_Billions.
    Returns:
    - plots_iso_lof_gdp_anomalies.png
    """

    # Subplots
    fig, axes = plt.subplots(1, 2, figsize=(14,5))

    # GDP Anomalies - LOF
    normal = df[df['GDP_LOF_Label'] == 1]
    anomalies = df[df['GDP_LOF_Label'] == -1]
    axes[0].scatter(normal['GDP_A_Billions'], normal['GDP_B_Billions'], 
                    c='yellow', edgecolor = 'green')
    axes[0].scatter(anomalies['GDP_A_Billions'], anomalies['GDP_B_Billions'], 
                    c='purple', edgecolor='#4B0082')
    axes[0].set_title('GDP Anomalies - LOF')
    axes[0].set_xlabel('GDP_A_Billions')
    axes[0].set_ylabel('GDP_B_Billions')

    # GDP Loss Anomalies - LOF
    normal1 = df[df['GDP_Loss_LOF_Label'] == 1]
    anomalies1 = df[df['GDP_Loss_LOF_Label'] == -1]
    axes[1].scatter(normal1['GDP_Loss_Ratio'], normal1['Economic_Loss_USD_Billions'], 
                    c='yellow', edgecolor='green')
    axes[1].scatter(anomalies1['GDP_Loss_Ratio'], anomalies1['Economic_Loss_USD_Billions'], 
                    c='purple', edgecolor='#4B0082')
    axes[1].set_title('GDP Loss Anomalies - LOF')
    axes[1].set_xlabel('GDP_Loss_Ratio')
    axes[1].set_ylabel('Economic_Loss_USD_Billions')
    
    plt.tight_layout()

    return fig


