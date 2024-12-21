import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
def load_data(file_path):
    '''
    Loads data from a CSV file into a pandas DataFrame.
    Args:
        file_path (str): The path to the CSV file to be loaded.
    Returns:
        pandas.DataFrame: A DataFrame containing the loaded data.
    Prints:
        A message indicating the number of rows loaded from the file.
    '''
    data = pd.read_csv(file_path)
    print(f"Loaded {len(data)} rows from {file_path}")
    return data

# Handle missing values
def handle_missing_values(data):
    '''
    Replaces missing values in a DataFrame with median/mode values.
    Args:
        data (pandas.DataFrame): The DataFrame to be processed.
    Returns:
        pandas.DataFrame: A DataFrame with missing values replaced.
    Prints:
        A message indicating the number of rows after handling missing values.
    '''
    data['house_size'].fillna(data['house_size'].median(), inplace=True)
    data['acre_lot'].fillna(data['acre_lot'].median(), inplace=True)
    data['street'].fillna(data['street'].mode()[0], inplace=True)
    data['price'].fillna(data['price'].median(), inplace=True)
    data['bed'].fillna(data['bed'].median(), inplace=True)
    data['bath'].fillna(data['bath'].median(), inplace=True)
    data['prev_sold_date'] = pd.to_datetime(data['prev_sold_date'], errors='coerce')
    print(f"After handling missing values: {len(data)} rows")
    return data

# Convert 'prev_sold_date' into 'years_since_last_sold' feature
def add_years_since_last_sold(data):
    '''
    Calculates the number of years between the current date and a given date
    (in the 'prev_sold_date' column) and adds it as a new feature
    ('years_since_last_sold') to the DataFrame.
    Args:
        data (pandas.DataFrame): The DataFrame to be processed.
    Returns:
        pandas.DataFrame: A DataFrame with the new feature added.
    Prints:
        A message indicating the number of rows after adding the new feature.
    '''
    today = pd.Timestamp.today()
    data['years_since_last_sold'] = data['prev_sold_date'].apply(lambda x: (today - x).days / 365 if pd.notnull(x) else 0)
    print(f"After adding years since last sold: {len(data)} rows")
    return data

# Encode categorical columns
def encode_categorical_columns(data, column):
    '''
    Encodes a categorical column in a DataFrame using a LabelEncoder.
    Args:
        data (pandas.DataFrame): The DataFrame to be processed.
        column (str): The name of the categorical column to be encoded.
    Returns:
        pandas.DataFrame: A DataFrame with the new encoded feature added.
    Prints:
        A message indicating the number of rows after encoding the categorical column.
    '''
    le = LabelEncoder()
    data[f'{column}_encoded'] = le.fit_transform(data[column])
    print(f"After encoding categorical column '{column}': {len(data)} rows")
    return data

# Remove rows with any remaining NaN values
def remove_nan_rows(data):
    '''
    Removes any rows with NaN values from a DataFrame.
    Args:
        data (pandas.DataFrame): The DataFrame to be cleaned.
    Returns:
        pandas.DataFrame: A DataFrame with all NaN rows removed.
    Prints:
        A message indicating the number of rows after removing NaN rows.
    '''
    cleaned_data = data.dropna()
    print(f"After removing NaN rows: {len(cleaned_data)} rows")
    return cleaned_data