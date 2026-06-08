
def conflict_type_validation(df):
    
    """
    Function is a basic fact check on conflict types. Is not applied as a filter due to only 45 valid rows as an output.
    # 'Cold Conflict' should have low death toll, no nuclear weapon, low air strikes and naval battles count; ceasefire should be true.
    # 'Civil War' should involve the same country on both sides of the conflict.
    # 'Skirmish' should have minimal economic loss.    
    Returns:
    - Conflict_Type_Valid: Binary indicator of whether the conflict type is valid (1) or not (0) for each row in the dataset.
    """
    
    df['Conflict_Type_Valid'] = 1
    #Setup default value for conflict type validation column, as not every conflict type was included in fact_checks
    
    def fact_checks(row):
        if row['Conflict_Type'] == 'Cold Conflict':
            return (
                1 if (
                    (row['Military_Deaths_A'] + row['Military_Deaths_B'] + row['Civilian_Deaths'] <= 100) &
                    (row['Weapons_Used'] != 'Nuclear') &
                    (row['Air_Strikes'] <= 50) &
                    (row['Naval_Battles'] <= 20) &
                    (row['Ceasefire'] == 1)
                )
                else 0
            )
        elif row['Conflict_Type'] == 'Civil War':
            return 1 if (row['Country_A'] == row['Country_B']) else 0
        elif row['Conflict_Type'] == 'Skirmish':
            return 1 if (row['Economic_Loss_USD_Billions'] < 0.1) else 0
        else:
            return 0
        
    df['Conflict_Type_Valid'] = df.apply(fact_checks, axis = 1)

    return df

# Conflict_Type_Valid
# 0    2955
# 1      45
