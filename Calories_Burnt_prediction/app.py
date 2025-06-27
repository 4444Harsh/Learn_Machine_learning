# app.py
import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('xgb_calorie_predictor.pkl')

st.title("Calorie Burn Prediction App")

st.markdown("### Enter the Exercise Details")

# Input features
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
height = st.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
duration = st.number_input("Exercise Duration (in minutes)", min_value=0, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=50, max_value=200, value=100)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0, value=37.0)

# Convert gender to numeric
gender = 0 if gender.lower() == "male" else 1

# Predict
if st.button("Predict Calories Burned"):
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f} kcal")
