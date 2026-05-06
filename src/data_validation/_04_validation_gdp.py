
def gdp_validation(df, country_gdp_billions):
    
    """
    Based on country current GDP - saved for each country in config file as a dictionary - 
    this function checks if GPD values provided in the dataset are less or equal to current GDP per country.
    The function is not applied as filter as it resulted in only 118 valid rows out of 3000.
    Returns:
    - GDP_Valid: Binary indicator of whether GDP values for both Country_A and Country_B are valid (1) or not (0).
    """
    # Returns True if country exists in the dictionary and GDP value is listed under  that country.
    def country_in_dictionary_check(country, gdp):
        if not isinstance(country, str):
            return False
        elif country not in country_gdp_billions:
            return False
        return gdp <= country_gdp_billions[country]
    
    # Returns 1 if GDP values for both Country_A and Country_B are valid, 0 otherwise.
    def validate_rule(row):
        valid_A = country_in_dictionary_check(row['Country_A'], row['GDP_A_Billions'])
        valid_B = country_in_dictionary_check(row['Country_B'], row['GDP_B_Billions'])
        return 1 if (valid_A and valid_B) else 0
    
    # Apply the GDP validation function to each row and create 'GDP_Valid' column
    df['GDP_Valid'] = df.apply(validate_rule, axis = 1)

    return df

# GDP_Valid
# 0    2882
# 1     118
