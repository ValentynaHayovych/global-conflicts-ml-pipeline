import matplotlib.pyplot as plt

# War defender lost
def war_defendor_lost(df, adf):

    """
    Function creates barcharts of countries that were the defenders and defeated
    with visual comparison between raw and filtered dataset, 
    included also Year_Valid and Population_Valid validations as filters.
    Returns:
    - war_defendor_lost.png
    """

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    raw_counts = df[df['Outcome'] == 'Victory_A']['Country_B'].value_counts()
    axes[0].bar(raw_counts.index, raw_counts.values, color = '#33C0CC')
    axes[0].set_title('War Defender losses (raw data)')
    axes[0].set_xlabel('Defender (Country_B)')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    yeva = adf[adf['Year_Valid'] == 1] # added year filtering 
    pova = yeva[yeva['Population_Valid'] == 1] # added population filtering

    valid_counts = pova[pova['Outcome'] == 'Victory_A']['Country_B'].value_counts()
    axes[1].bar(valid_counts.index, valid_counts.values, color = '#28DEED')
    axes[1].set_title('Defender losses (validated data)')
    axes[1].set_xlabel('Defender (Country_B)')
    axes[1].set_ylabel('Count')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    return fig