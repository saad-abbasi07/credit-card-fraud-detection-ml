import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("fraud_model.pkl")

st.title("🛡️ Credit Card Fraud Detector")

# Create input fields for all 30 features
with st.form("prediction_form"):
    st.write("Enter Transaction Details")
    # Example inputs (Add all V1-V28, Time, Amount as needed)
    time = st.number_input("Time", value=0.0)
    amount = st.number_input("Amount", value=0.0)
    v_features = [st.number_input(f"V{i}", value=0.0) for i in range(1, 29)]
    
    submitted = st.form_submit_button("Check for Fraud")

if submitted:
    # Prepare data for prediction
    data = np.array([[time] + v_features + [amount]])
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected!")
    else:
        st.success("Transaction is Legitimate.")