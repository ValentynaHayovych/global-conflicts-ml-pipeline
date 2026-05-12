from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def train_random_forest(df):

    """
    Builds predictive classification model Random Forest, 
    including preprocessing and hyperparameter tuning.
    Returns:
    - model and name
    """

    # Make comlumn output consistent with required type of output needed for binary analysis
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

    # Random Forest pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', RandomForestClassifier(
            n_estimators=100, 
            class_weight='balanced', 
            random_state=42
        ))
    ])

    # Random Forest estimators, max depth and samples split
    params = {
        'model__n_estimators': [100, 200],
        'model__max_depth': [None, 10, 20],
        'model__min_samples_split': [2,5]
        }
    
    model = GridSearchCV(
        pipeline, 
        params, 
        cv=5,
        scoring='f1_weighted'
        )

    return {
        'name': 'Random Forest',
        'model': model
    }
