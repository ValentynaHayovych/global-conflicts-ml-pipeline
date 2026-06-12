from src._03_anomaly_detection._01_ml_iso_population_analysis import iso_population_analysis
from src._03_anomaly_detection._02_ml_iso_gdp_analysis import iso_gdp_analysis
from src._03_anomaly_detection._03_ml_lof_gdp_analysis import gdp_lof_analysis
from src._03_anomaly_detection._04_ml_iso_coordinates_analysis import iso_coordinates_analysis
from src._03_anomaly_detection._05_ml_dbscan_deaths_coordinates_analysis import dbscan_deaths_coordinates_analysis

def anomaly_detection(vdf):
    vdf = iso_population_analysis(vdf)
    vdf = iso_gdp_analysis(vdf)
    vdf = gdp_lof_analysis(vdf)
    vdf = iso_coordinates_analysis(vdf)
    adf = dbscan_deaths_coordinates_analysis(vdf)

    return adf