import streamlit as st
import pandas as pd
from data_load_files import year, make, model, trim, body, transmission, state, color, interior
from Model import linear_model  # Ensure this function is correctly defined
import numpy as np
#from Model import loaded_encoder
from Model import Label_encoding_Feat_engr
from Model import linear_model_Object

# Set page configuration
st.set_page_config(page_title="Vehicle Price Predictor", layout="centered")

def create_GUI():
    # Header Section
    st.title("🚗 Vehicle Price Predictor")
    st.write("Predict the price of a vehicle based on its features.")

    # Input Section
    st.header("Input Vehicle Details")

    year_input = st.selectbox("Year of Manufacture", year)
    make_input = st.selectbox("Select Make", make)
    model_input = st.selectbox("Select Model", model)
    trim_input = st.selectbox("Trim Type", trim)
    body_input = st.selectbox("Body Type", body)
    transmission_input = st.selectbox("Transmission Type", transmission)
    state_input = st.selectbox("Select State", state)
    condition_input = st.text_input("Condition rate", "From 1.0 to 50.0")
    odometer_input = st.text_input("Odometer reading", "Enter Odometer reading")
    color_input = st.selectbox("Color", color)
    interior_input = st.selectbox("Interior", interior)
    mmr_input = st.text_input("Market Mannheim Report", "Enter mmr value")

    # Prediction Section
    st.header("Predicted Price")
    if st.button("Predict"):

        try:
            # Ensure year_input is an integer (it's selected from a dropdown)
            try:
                year_input = int(year_input)
            except ValueError:
                st.error("Invalid year selected. Please choose a valid year.")
                return

            # Try to convert condition_input to float and validate
            try:
                condition_input = float(condition_input)
                if not (0 <= condition_input <= 50):
                    st.error("Condition should be between 0 and 50.")
                    return
            except ValueError:
                st.error("Condition rate should be a number between 0 and 50.")
                return

            # Try to convert odometer_input to float and validate
            try:
                odometer_input = float(odometer_input)
                if not (odometer_input >= 0):
                    st.error("Odometer reading must be a positive value.")
                    return
            except ValueError:
                st.error("Odometer reading should be a numeric value.")
                return

            # Try to convert mmr_input to float and validate
            try:
                mmr_input = float(mmr_input)
                if not (mmr_input >= 0):
                    st.error("MMR value must be a positive number.")
                    return
            except ValueError:
                st.error("MMR value should be a numeric value.")
                return

            # If all inputs are valid, create the input data DataFrame
            input_data = pd.DataFrame({
                'year': [year_input],
                'make': [make_input],
                'model': [model_input],
                'trim': [trim_input],
                'body': [body_input],
                'transmission': [transmission_input],
                'state': [state_input],
                'condition': [condition_input],
                'odometer': [odometer_input],
                'color': [color_input],
                'interior': [interior_input],
                'mmr': [mmr_input],
            })

            # Call the prediction model

            # Apply label encoding
            df_encoded = Label_encoding_Feat_engr(input_data)
            print(df_encoded.shape)
            # Predict the result
            predicted_price = linear_model_Object(df_encoded, linear_model)
            print(predicted_price)
              # Make sure the function is defined correctly
            st.success(f"The predicted price is ${predicted_price:,.2f}")

        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

    else:
        st.info("Enter details and click Predict to see the price.")

    # Footer
    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

# Run the app
if __name__ == '__main__':
    create_GUI()