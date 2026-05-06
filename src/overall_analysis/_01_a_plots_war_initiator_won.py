import matplotlib.pyplot as plt

# War iniciator obtained victory
def war_initiator_won(df, adf):

    """
    Function creates barcharts of countries that were the aggressors and won
    with visual comparison between raw and filtered dataset, 
    included also Year_Valid and Population_Valid validations as filters.
    Returns:
    - war_initiator_won.png
    """

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    raw_counts = df[df['Outcome'] == 'Victory_A']['Country_A'].value_counts()
    axes[0].bar(raw_counts.index, raw_counts.values, color = '#D41C41')
    axes[0].set_title('War initiator obtained victory (raw data)')
    axes[0].set_xlabel('War Initiator (Country_A')
    axes[0].set_ylabel('Number of Victories')
    axes[0].tick_params(axis='x', rotation=45)

    yeva = adf[adf['Year_Valid'] == 1] # added year filtering 
    pova = yeva[yeva['Population_Valid'] == 1] # added population filtering

    valid_counts = pova[pova['Outcome'] == 'Victory_A']['Country_A'].value_counts()
    axes[1].bar(valid_counts.index, valid_counts.values, color = '#FC1E4A')
    axes[1].set_title('War initiator obtained victory (validated data)')
    axes[1].set_xlabel('War Initiator (Country_A)')
    axes[1].set_ylabel('Number of Victories')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    return fig



    