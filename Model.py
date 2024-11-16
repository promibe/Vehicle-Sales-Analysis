#necessary Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, FunctionTransformer

import joblib
import pickle

# Load the pipeline
linear_model = joblib.load('vehicle_sales_model.pkl')



input_data = pd.DataFrame({
                'year': [2015],
                'make': ['kia'],
                'model': ['Sorento'],
                'trim': ['LX'],
                'body': ['suv'],
                'transmission': ['automatic'],
                'state': ['ca'],
                'condition': [5.0],
                'odometer': [16639.0],
                'color': ['white'],
                'interior': ['black'],
                'mmr': [20500.0],
            })




# cat_col = [col for col in columns if df[col].dtypes in ['object']]
# print((cat_col))


def Label_encoding_Feat_engr(df):
    """
    Apply label encoding and feature engineering to specific columns in a DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame to encode and engineer.
        encoder (LabelEncoder): The pre-loaded label encoder.

    Returns:
        DataFrame: The DataFrame with encoded columns and new features.
    """
    # Check if required columns for feature engineering exist
    required_columns = ['odometer', 'mmr', 'condition']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Feature Engineering
    df['odo_mmr'] = df['odometer'] * df['mmr']
    df['mmr_cond'] = df['mmr'] * df['condition']
    df['odo_cond'] = df['condition'] * df['odometer']

    # Label Encoding
    columns_to_encode = ['make', 'model', 'trim', 'body', 'transmission', 'state', 'color', 'interior']
    # Load each encoder and apply it to the new data
    for column in columns_to_encode:
        with open(f"{column}_encoder.pkl", "rb") as file:
            loaded_encoder = pickle.load(file)
            df[column] = loaded_encoder.transform(df[column])

    # Display the transformed DataFrame
    #print("\nTransformed New DataFrame:")
    return df





def linear_model_Object(df, model):
    """
    Predict the result using a trained model and an encoded DataFrame.

    Parameters:
        df (DataFrame): The pre-processed DataFrame with label encoding applied.
        model: The trained machine learning model for prediction.

    Returns:
        float: The predicted result.
    """
    # Ensure the input DataFrame is not empty
    if df.empty:
        raise ValueError("The input DataFrame is empty. Cannot make predictions.")

    # Perform the prediction
    result = model.predict(df)
    if result is not None and isinstance(result, np.ndarray): #converting it to a scaler
        result = result[0]
    return result


#linear_model(input_data)

#print(linear_model(input_data))

#en = Label_encoding_Feat_engr(input_data)

#print(linear_model_Object(en, linear_model))
