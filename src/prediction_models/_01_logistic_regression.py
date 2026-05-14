from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

def train_logistic_regression(df):

    """
    Builds predictive classification model Logistic Regression, 
    including preprocessing and hyperparameter tuning.
    Returns:
    - model and name
    """
    
    df = df.copy()
    
    # Make column output consistent with required type of output needed for binary analysis
    df['UN_Involvement'] = df['UN_Involvement'].map({
        'yes': 1,
        'no': 0,
        '1': 1,
        '0': 0,
        'NA': 0,
    })

    # Ensuring no Nan values and column type of values setup to integer
    df['UN_Involvement'] = df['UN_Involvement'].fillna(0).astype(int)

    # Define columns groups
    num_cols = ['GDP_A_Billions', 'GDP_B_Billions', 'Economic_Loss_USD_Billions']
    cat_cols = ['Conflict_Type', 'Alliance_A', 'Alliance_B', 'Resource_Dispute']
    bin_cols = ['UN_Involvement']

    # Preprocessor
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('bin', 'passthrough', bin_cols)
    ])

    # Logistic Regression pipeline
    pipeline = Pipeline([    
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(
            max_iter=1000, 
            class_weight = 'balanced' 
        ))
    ])

    # 8 parameter combinations
    params = { 
        'classifier__C': [0.01, 0.1, 1, 10], 
        'classifier__solver': ['lbfgs', 'saga'] 
        }
    
    grid_search = GridSearchCV(
        pipeline, 
        params, 
        cv=5, # cross-validation folds
        scoring='accuracy'
        )
    
    return {
        'name': 'Logistic Regression',
        'model': grid_search
    }
