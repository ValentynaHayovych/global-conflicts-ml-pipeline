import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def final_ml_data_validation(adf):

    """
    Function creates validation matrix to sum up all the validations and machine learning applied models.
    Returns:
    - final_data_validation.png
    """

    valid_columns = ['Total_Deaths_Valid', 'GDP_IF_Valid', 'GDP_Loss_IF_Valid', 'GDP_LOF_Valid', 'GDP_Loss_LOF_Valid',
                     'Coords_IF_Valid', 'Coords_DBSCAN_Valid', 'Total_Deaths_DBSCAN_Valid']
    
    countries = pd.concat([
        adf[['Country_A'] + valid_columns].rename(columns={'Country_A': 'Country'}),
        adf[['Country_B'] + valid_columns].rename(columns={'Country_B': 'Country'})
    ])

    table = countries.groupby('Country')[valid_columns].sum().astype(int)
    table['Score'] = table[valid_columns].mean(axis=1).round(2)
    table = table.sort_values(by='Score', ascending=False)

    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(table.T, cmap='YlGnBu', ax=ax, annot=True, fmt='.0f', annot_kws={'size':7})
    ax.set_title('ML Validation Matrix')

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig

