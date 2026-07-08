# CreditWise: Loan Approval Prediction System

## Overview

CreditWise is an end-to-end Machine Learning project that predicts loan approval decisions based on an applicant's financial, demographic, and employment-related information.

The project follows a complete ML workflow including data preprocessing, feature engineering, model training, performance evaluation, and deployment through a Streamlit web application.

---

## Problem Statement

Financial institutions process numerous loan applications daily. Manual evaluation can be time-consuming and inconsistent.

This project aims to build a predictive system that assists in assessing an applicant's creditworthiness and likelihood of loan approval using historical applicant data.

---

## Dataset Features

### Financial Features

- Applicant Income
- Coapplicant Income
- Savings
- Existing Loans
- Collateral Value
- Loan Amount
- Loan Term

### Demographic Features

- Age
- Gender
- Marital Status
- Dependents
- Education Level

### Employment Features

- Employment Status
- Employer Category

### Loan Information

- Loan Purpose
- Property Area
- Credit Score

---

## Data Preprocessing

The following preprocessing techniques were applied:

### Label Encoding

- Education_Level
- Loan_Approved

### One-Hot Encoding

- Employment_Status
- Marital_Status
- Loan_Purpose
- Property_Area
- Gender
- Employer_Category

### Feature Engineering

Additional derived features were created:

- DTI_Ratio_sq
- Credit_Score_sq

These engineered features helped capture non-linear relationships in the data.

---

## Machine Learning Models Evaluated

The project compares multiple classification algorithms:

### Logistic Regression

Used as a baseline linear classification model.

### Decision Tree Classifier

Captures non-linear decision boundaries and feature interactions.

### Random Forest Classifier

Ensemble-based approach combining multiple decision trees to improve generalization and predictive performance.

---

## Model Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

A comparative analysis was performed to identify the best-performing model.

---

## Final Model

**Random Forest Classifier** was selected as the final model based on its overall predictive performance and robustness.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

## Project Structure

Creditwise Loan Approval/
│
├── app.py
├── loan_model.pkl
├── ohe.pkl
├── label_encoder.pkl
├── requirements.txt
├── CreditWise_Loan_Approval.ipynb
└── README.md

---

## Streamlit Application

The deployed application allows users to:

- Enter applicant details
- Select demographic and employment information
- Generate real-time loan approval predictions
- Assess applicant creditworthiness

---

## Key Learning Outcomes

- Data preprocessing and encoding techniques
- Feature engineering
- Supervised Machine Learning
- Model comparison and evaluation
- Ensemble learning using Random Forest
- Model serialization with Joblib
- Web application deployment using Streamlit
- Version control with Git and GitHub

---

## Future Improvements

- Hyperparameter tuning
- Probability-based risk scoring
- Explainable AI using SHAP
- Integration with real-world banking datasets
- Cloud deployment and monitoring

---

## Author
Vanshika  
Master of Computer Applications (AI & IoT)  
National Institute of Technology Patna
