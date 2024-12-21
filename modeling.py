from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
import numpy as np

def predictive_modeling(data):
    """
    Performs predictive modeling using linear regression on the provided dataset.

    This function selects relevant features, splits the data into training and testing sets, 
    trains a linear regression model, makes predictions, and evaluates the model's performance. 
    The evaluation metrics are saved to a text file.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be modeled. It must include the columns:
        'house_size', 'acre_lot', 'years_since_last_sold', 'status_encoded', 'bed', 'bath', 
        and 'price'.

    Returns
    -------
    None
    """
    # Features and target variable
    features = ['house_size', 'acre_lot', 'years_since_last_sold', 'status_encoded', 'bed', 'bath']
    X = data[features]
    y = data['price']

    # Check if dataset is empty
    if X.empty or y.empty:
        print("Dataset is empty after preprocessing. Exiting.")
        return

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    # Print evaluation metrics
    #print(f'Mean Absolute Error: {mae:.2f}')
    #print(f'Mean Squared Error: {mse:.2f}')
    #print(f'Root Mean Squared Error: {rmse:.2f}')

    # Save evaluation metrics to a text file
    with open('analyses_output/model_evaluation.txt', 'w') as f:
        f.write('Model Evaluation Metrics\n')
        f.write('========================\n')
        f.write(f'Mean Absolute Error: {mae:.2f}\n')
        f.write(f'Mean Squared Error: {mse:.2f}\n')
        f.write(f'Root Mean Squared Error: {rmse:.2f}\n')