from config.country_metrics import country_gdp_millions
from config.country_metrics import country_independence_year
from config.country_metrics import country_population
from config.country_metrics import country_bounds

from src.data_validation._01_validation_conflict_type import conflict_type_validation
from src.data_validation._02_validation_year import year_validation
from src.data_validation._03_validation_population import population_validation
from src.data_validation._04_validation_gdp import gdp_validation
from src.data_validation._05_validation_conflict_coordinates import conflict_coordinates_validation
from src.data_validation._06_conflict_coordinates_land_only import conflict_coordinates_land_only

import pandas as pd
    
def validate_data(df):
    
    df = conflict_type_validation(df)
    df = year_validation(df, country_independence_year)
    df = population_validation(df, country_population)
    df = gdp_validation(df, country_gdp_millions)
    df = conflict_coordinates_validation(df, country_bounds)
    vdf = conflict_coordinates_land_only(df)

    """
    Terminal printout for all the validated results per column
    """
    valid_cols = [col for col in df.columns if col.endswith('_Valid')]

    summary = pd.DataFrame({
        'metric': valid_cols,
        'valid_n': [df[col].sum() for col in valid_cols],
        'total_n': len(df)
    })

    summary['valid_%'] = (summary['valid_n'] / summary['total_n'] * 100).round(2)

    table = summary[['metric', 'valid_n', 'valid_%']]

    print('Sum of validated dataset metrics:')
    print('-'*50)
    print(table.to_string(index=False))
    print('-'*50)

    return vdf

