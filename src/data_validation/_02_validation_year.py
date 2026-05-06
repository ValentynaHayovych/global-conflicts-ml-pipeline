
def year_validation(df, country_independence_year):

    """
    Checks if a country existed in the given year.
    Based on the country independence year provided in dictionary of the config file country_metrics.
    The function is applied as a filter for final analysis - Total War Involvment.
    Returns:
    - Year_Valid: Binary indicator of whether the year of conflict is valid (1) or not (0) for both Country_A and Country_B.
    """

    def rule_year_check(country, year):
        return country in country_independence_year and country_independence_year[country] <= year
    
    def valid_year(row):
        valid_y_A = rule_year_check(row['Country_A'], row['Year'])
        valid_y_B = rule_year_check(row['Country_B'], row['Year'])
        return 1 if (valid_y_A + valid_y_B) else 0
    
    df['Year_Valid'] = df.apply(valid_year, axis=1)

    return df

# Year_Valid
# 1    2928
# 0     72