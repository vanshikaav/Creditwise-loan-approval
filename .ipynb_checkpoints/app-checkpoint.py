import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")

st.title("CreditWise Loan Approval System")

# Numeric Inputs
income = st.number_input("Applicant Income", min_value=0.0)
co_income = st.number_input("Coapplicant Income", min_value=0.0)
age = st.number_input("Age", min_value=18)
dependents = st.number_input("Dependents", min_value=0)
existing_loans = st.number_input("Existing Loans", min_value=0)
savings = st.number_input("Savings", min_value=0.0)
collateral = st.number_input("Collateral Value", min_value=0.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
loan_term = st.number_input("Loan Term (months)", min_value=1)

education = st.selectbox(
    "Education Level",
    ["Graduate", "Not Graduate"]
)

employment = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-employed", "Unemployed"]
)

marital = st.selectbox(
    "Marital Status",
    ["Married", "Single"]
)

purpose = st.selectbox(
    "Loan Purpose",
    ["Car", "Education", "Home", "Personal"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

employer = st.selectbox(
    "Employer Category",
    ["Government", "MNC", "Private", "Unemployed"]
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900
)

if st.button("Predict"):

    row = {
        "Applicant_Income": income,
        "Coapplicant_Income": co_income,
        "Age": age,
        "Dependents": dependents,
        "Existing_Loans": existing_loans,
        "Savings": savings,
        "Collateral_Value": collateral,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Education_Level": 1 if education == "Graduate" else 0,

        "Employment_Status_Salaried": 1 if employment=="Salaried" else 0,
        "Employment_Status_Self-employed": 1 if employment=="Self-employed" else 0,
        "Employment_Status_Unemployed": 1 if employment=="Unemployed" else 0,

        "Marital_Status_Single": 1 if marital=="Single" else 0,

        "Loan_Purpose_Car": 1 if purpose=="Car" else 0,
        "Loan_Purpose_Education": 1 if purpose=="Education" else 0,
        "Loan_Purpose_Home": 1 if purpose=="Home" else 0,
        "Loan_Purpose_Personal": 1 if purpose=="Personal" else 0,

        "Property_Area_Semiurban": 1 if property_area=="Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area=="Urban" else 0,

        "Gender_Male": 1 if gender=="Male" else 0,

        "Employer_Category_Government": 1 if employer=="Government" else 0,
        "Employer_Category_MNC": 1 if employer=="MNC" else 0,
        "Employer_Category_Private": 1 if employer=="Private" else 0,
        "Employer_Category_Unemployed": 1 if employer=="Unemployed" else 0,

        "DTI_Ratio_sq": (loan_amount / max(income,1))**2,
        "Cedit_Score_sq": credit_score**2
    }

    X = pd.DataFrame([row])

    prediction = model.predict(X)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")