
def conflict_coordinates_validation(df, country_bounds):

    """"
    Based on country bounds - square zones for each country saved in config file as a dictionary - 
    this function checks weather conflict coordinates land within one of two conflicted countries.
    The function is not applied as filter as it resulted in only 8 valid coordinates out of 3000.
    Returns:
    - Conflict_Coordinates_Valid: Binary indicator of whether conflict coordinates land within one 
    of two conflicted countries' zones.
    """

    def conflict_coordinates(row, country_col, lat_col, lon_col):
        """
        Checks if single row's coordinates lie within country bounds (taken from config file country_metrics).
        """
        country = row[country_col] # Get the country name from the specified column in the row
        lat = row[lat_col] # Get the latitude value from the specified column in the row
        lon = row[lon_col] # Get the longitude value from the specified column in the row

        if country not in country_bounds:  # If the country is not in the country_bounds dictionary, we cannot validate the coordinates, so we return 0 (invalid)
            return 0
        
        bounds = country_bounds[country] # bounds is a dictionary with 'lat' and 'lon' keys, each containing a tuple of (min, max) values
        lat_ok = bounds['lat'][0] <= lat <= bounds['lat'][1] # Check if latitude is within bounds
        lon_ok = bounds['lon'][0] <= lon <= bounds['lon'][1] # Check if longitude is within bounds

        return 1 if (lat_ok and lon_ok) else 0

    # Apply the conflict_coordinates function to each row for both Country_A and Country_B and create 'Conflict_Coordinates_Valid' column
    df['Conflict_Coordinates_Valid'] = df.apply(
        lambda row: 1 if(
            conflict_coordinates(row, 'Country_A', 'Latitude', 'Longitude') and
            conflict_coordinates(row, 'Country_B', 'Latitude', 'Longitude')             
        ) else 0,
        axis=1
    )

    return df

# Conflict_Coordinates_Valid
# 0    2992
# 1       8