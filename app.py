import pandas as pd
import numpy as np
import streamlit as st
import joblib

scaler = joblib.load("scaler.pkl")
le_sex = joblib.load("label_encoders_sex.pkl")
le_smoker = joblib.load("label_encoders_smoker.pkl")
model = joblib.load("best_model.pkl")

st.set_page_config(page_title = "Insurance charges Predictor", layout = "centered")
st.title("Health Insurance Payment Prediction App")
st.write("Enter the details below to estimate your insurance payment amount")

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value = 0, max_value = 100, value = 30)
        bmi = st.number_input("BMI", min_value = 10.0, max_value = 60.0, value = 20.0)
        children = st.number_input("Number of Children", min_value = 0, max_value = 8, value = 0)
    with col2:
        sex = st.selectbox("sex", options = le_sex.classes_)
        smoker = st.selectbox("Smoker", options = le_smoker.classes_)
        
    submitted = st.form_submit_button("Predict Payment")

if submitted:

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker]
    })

    input_data["sex"] = le_sex.transform(input_data["sex"])
    input_data["smoker"] = le_smoker.transform(input_data["smoker"])

    num_cols = ["age", "bmi", "children"]
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    prediction = model.predict(input_data)[0]

    st.success(f"**Estimated Insurance Payment Amount:** ₹{prediction:,.2f}")