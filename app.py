import streamlit as st
import joblib
import os
import pickle
import numpy as np

# Load the model
model = joblib.load(f'{working_dir}/xgb_best_model.joblib', 'rb')


# Set page config
st.set_page_config(
    page_title="Air Quality Prediction",
    layout="wide",
    page_icon="🌫️",
)

# Center the title
st.markdown(
    "<h1 style='text-align: center; color: black;'>AQI Prediction</h1>",
    unsafe_allow_html=True,
)

# Center the descriptive text
st.markdown(
    """
    <p style='text-align: center;'>
        To help predict the Air Quality Index (AQI), please provide the following information:
    </p>
    """,
    unsafe_allow_html=True,
)


col1, col2, col3 = st.columns(3)


with col1:
    feature_1 = st.number_input("Avg Temp (°C)", min_value=0.0, value=0.0)
    feature_2 = st.number_input("Max Temp (°C)", min_value=0.0, value=0.0)
    feature_3 = st.number_input("Min Temp (°C)", min_value=0.0, value=0.0)

with col2:
    feature_4 = st.number_input("Pressure (hPa)", min_value=0.0, value=0.0)
    feature_5 = st.number_input("Humidity (%)", min_value=0.0, value=0.0)
    feature_6 = st.number_input("Visibility (km)", min_value=0.0, value=0.0)

with col3:
    feature_7 = st.number_input("Avg Windspeed (km/h)", min_value=0.0, value=0.0)
    feature_8 = st.number_input("Max Windspeed (km/h)", min_value=0.0, value=0.0)

# Center-align the Predict button
st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
if st.button("Predict AQI"):
    aqi_input = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8]])
    if all(aqi_input[0]):  # Check if all input features are provided
        aqi_prediction = model.predict(aqi_input)
        st.success(f"Predicted AQI: {aqi_prediction[0]}")
    else:
        st.error("Please enter values for all AQI features.")
st.markdown("</div>", unsafe_allow_html=True)