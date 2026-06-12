import pandas as pd

def load_data(file_path):

    """
    Loads the .csv dataset from the file path provided in main.
    Returns a dataframe.
    """
    df = pd.read_csv(file_path) 
    
    if df.empty:
        raise ValueError("Issue with loading data.")
    else:      
        return df