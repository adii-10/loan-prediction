import pickle
import streamlit as st
import pandas as pd

loan_model = pickle.load(open("loan_prediction_model.pkl", "rb"))

st.title("Loan Prediction")

gender = st.number_input("Gender: 0-Female, 1-Male", value=None)
married = st.number_input("Married: 0-No, 1-Yes", value=None)
dependents = st.number_input("Dependents: 1-4", value=None)
education = st.number_input("Education: 0-Not Graduate, 1-Graduate", value=None)
self_employed = st.number_input("Self_Employed: 0-No,1-Yes", value=None)
applicant_income = st.number_input("Applicant_Income: Multiple of 1000$", value=None)
coapplicant_income = st.number_input("Coapplicant_Income: Multiple of 1000$", value=None)
loan_amount = st.number_input("Loan Amount: Multiple of 1000$", value=None)
loan_amount_term = st.number_input("Loan Amount Term: No of months", value=None)
credit_history = st.number_input("Credit History: 1/0", value=None)
property_area = st.number_input("Property Area: 0-Rural,1-Urban,2-Semi-Urban", value=None)

# Placeholder for result
result_placeholder = st.empty()

if st.button("Predict"):
    # Check if all required fields are filled
    if None in [gender, married, dependents, education, self_employed, applicant_income,
                coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]:
        result_placeholder.error("Please fill in all the fields.")
    else:
        df = pd.DataFrame({
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_amount_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }, index=[0])

        md_pred = loan_model.predict(df)
        if md_pred == 1:
            prediction = "Loan Approved"
        else:
            prediction = "Loan Rejected"

        result_placeholder.success(prediction)
