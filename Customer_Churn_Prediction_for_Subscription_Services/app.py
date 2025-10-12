import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('churn_model.pkl')

st.title('Customer Churn Prediction')
st.write('Enter customer details to predict churn')

# Create input fields
tenure = st.number_input('Tenure (months)', min_value=0, max_value=72)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0)
contract_type = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

if st.button('Predict Churn'):
    # Preprocess and predict
    prediction = model.predict([[tenure, monthly_charges, total_charges, contract_type]])
    st.write(f'Churn Prediction: {"Yes" if prediction[0] == 1 else "No"}')


import joblib
joblib.save(model, 'churn_model.pkl')
