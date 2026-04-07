import streamlit as st
import pandas as pd
import joblib
import numpy as np


model = joblib.load('crop_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🌱 Crop Recommendation System")
st.write("Input the environmental conditions to get the best crop recommendation.")


temp = st.slider("Temperature (°C)", 5.0, 50.0, 25.0)
hum = st.slider("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.slider("Soil pH", 3.0, 10.0, 6.5)
rain = st.slider("Rainfall (mm)", 20.0, 6000.0, 500.0)

if st.button("Predict Best Crop"):
    features = np.array([[temp, hum, ph, rain]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    st.success(f"The recommended crop is: **{prediction[0]}**")
