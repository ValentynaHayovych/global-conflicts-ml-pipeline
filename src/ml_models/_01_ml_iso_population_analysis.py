from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def iso_population_analysis(df):
    
    """
    Analyses death-related columns using Isolation Forest.

    Returns:
        - Total_Deaths: Sum of Military_Deaths_A, Military_Deaths_B, and Civilian_Deaths.
        - Civilian_Ratio: share of civilian deaths to total deaths.
        - Civ_Deaths_IF_Score: Isolation Forest score for civilian deaths.
        - Mil_Deaths_IF_Score: Isolation Forest score for military deaths. 
        - Civ_Deaths_Valid: Binary indicator of whether civilian deaths are valid (1) or anomalous (0).
        - Mil_Deaths_Valid: Binary indicator of whether military deaths are valid (1) or anomalous (0).
        - Total_Deaths_Valid: Binary indicator of whether total deaths are valid (1) or anomalous (0) based on scaled total deaths and population.
    """

    df['Total_Deaths'] = df['Military_Deaths_A'] + df['Military_Deaths_B'] + df['Civilian_Deaths']
    df['Civilian_Ratio'] = df['Civilian_Deaths'] / df['Total_Deaths']

    df['Military_Deaths_Ratio_A'] = df['Military_Deaths_A'] / df['Population_A_Millions']
    df['Military_Deaths_Ratio_B'] = df['Military_Deaths_B'] / df['Population_B_Millions']
 
    iso = IsolationForest(n_estimators=100, contamination = 0.03, random_state=42)

    df['Civilian_Deaths_IF_Label'] = iso.fit_predict(df[['Civilian_Ratio', 'Total_Deaths']])
    df['Military_Deaths_IF_Label'] = iso.fit_predict(df[['Military_Deaths_Ratio_A', 'Military_Deaths_Ratio_B']])

    df['Civ_Deaths_Valid'] = (df['Civilian_Deaths_IF_Label'] == 1).astype(int)
    df['Mil_Deaths_Valid'] = (df['Military_Deaths_IF_Label'] == 1).astype(int)

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['Total_Deaths', 'Population_A_Millions', 'Population_B_Millions']])
    df['Total_Deaths_Valid'] = (iso.fit_predict(scaled) == 1).astype(int)

    return df