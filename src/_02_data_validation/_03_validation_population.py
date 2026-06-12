
def population_validation(df, country_population):

    """
    Function checks if population values provided in the dataset are less or equal to current population 
    per country based on the data saved in dictionary of config file country_metrics.
    The function is applied as a filter for final analysis - Total War Involvment.
    Returns:
    - Population_Valid: Binary indicator of whether population values for both Country_A and Country_B are valid (1) or not (0).
    """
    # Returns True if country exists in the dictionary and population value is listed under that country.
    def rule_check(country, population):
        return country in country_population and population <= country_population[country] 
    
    # Returns 1 if population values for both Country_A and Country_B are valid, 0 otherwise.
    def pop_valid(row):
        pop_valid_A = rule_check(row['Country_A'], row['Population_A_Millions'])
        pop_valid_B = rule_check(row['Country_B'], row['Population_B_Millions'])
        return 1 if (pop_valid_A + pop_valid_B) else 0
    
    # Apply the population validation function to each row and create 'Population_Valid' column
    df['Population_Valid'] = df.apply(pop_valid, axis=1)

    return df

# Population_Valid
# 0    1941
# 1    1059