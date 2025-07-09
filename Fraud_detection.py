import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

# Load trained pipeline and threshold
pipeline = joblib.load('fraud_detection_pipeline.pkl')

with open("best_threshold.json", "r") as f:
    best_thresh = json.load(f)["threshold"]

# App title and description
st.title("💳 Fraud Detection App")
st.markdown("Please enter the transaction details and click **Predict** to assess fraud risk.")
st.divider()

# User input form
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0)


oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0, step=100.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0, step=100.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0, step=100.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0, step=100.0)

# Predict on submit
if st.button("Predict"):
    # Construct input DataFrame
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
       
    }])

    # Predict probability and apply custom threshold
    proba = pipeline.predict_proba(input_data)[0][1]
    prediction = int(proba >= best_thresh)

    st.write(f"**Probability of Fraud:** `{proba:.4f}`")
    if prediction == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Transaction Looks Safe")
