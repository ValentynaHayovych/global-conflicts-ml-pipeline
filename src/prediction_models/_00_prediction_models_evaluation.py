from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from src.prediction_models._01_logistic_regression import train_logistic_regression
from src.prediction_models._02_random_forest import train_random_forest

def evaluate_prediction_models(df):

    """
    Builds and evaluates predictive classification models using Logistic Regression and Random Forest, 
    including preprocessing, hyperparameter tuning and performance evaluation for each model.
    Returns:
     - performance reports
    """

    models = [
        train_logistic_regression(df),
        train_random_forest(df)
    ]

    for model_config in models:
        model = model_config['model']
        name = model_config['name']

        X = df.drop('Sanctions', axis=1)
        y = df['Sanctions']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        print(f"{name}:".center(60))
        print('Model best parameters:')
        print(model.best_params_)
        print('-'*60)
        print(classification_report(y_test, y_pred))
        print('-'*60)
