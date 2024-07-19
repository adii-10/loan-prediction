# Loan Prediction using Machine Learning

## Overview

The Loan Prediction System is a machine learning project that aims to predict the approval status of loan applications based on various applicant details. By leveraging historical data and machine learning algorithms, this system helps financial institutions make informed decisions.

## Features

- Predicts loan approval status based on applicant details.
- Utilizes multiple machine learning algorithms to find the most accurate predictions.
- Provides insights into the factors affecting loan approval.

## Methodology

The project follows these steps:
1. **Data Set Collection**: Gathered loan application data with attributes like Gender, Married, Dependents, Education, etc.
2. **Data Set Analysis**: Analyzed the dataset to understand the distribution and relationships between features.
3. **Data Cleaning and Structuring**: Handled missing values and structured the data for analysis.
4. **Handling Categorical Values**: Encoded categorical variables to numerical values.
5. **Applying Algorithms**: Implemented Logistic Regression, Support Vector Classifier (SVC), and Random Forest algorithms.
6. **Evaluating Accuracy**: Performed hyperparameter tuning and evaluated the accuracy of each model.
7. **Using Most Accurate Algorithm for Prediction**: Selected the Random Forest algorithm due to its highest accuracy for final predictions.

## Algorithms Used

- **Logistic Regression**
- **Support Vector Classifier (SVC)**
- **Random Forest** (Selected for final prediction due to highest accuracy)

## Dataset Details

- **Loan_ID**: Unique Identifier for each loan.
- **Gender**: Gender of the applicant.
- **Married**: Marital status of the applicant.
- **Dependents**: Number of dependents of the applicant.
- **Education**: Education level of the applicant.
- **Self_Employed**: Self-employment status of the applicant.
- **ApplicantIncome**: Income of the applicant.
- **CoapplicantIncome**: Income of the co-applicant.
- **LoanAmount**: Loan amount requested.
- **Loan_Amount_Term**: Term of the loan in months.
- **Credit_History**: Credit history of the applicant.
- **Property_Area**: Area type of the property (Urban/Semi-Urban/Rural).
- **Loan_Status**: Status of the loan (Approved/Not Approved).

## Technologies Used

- **Python**: Programming language for implementing the algorithms.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning library for implementing algorithms.
- **Jupyter Notebook**: Development environment.
- **Streamlit**: Deployment of the application for interactive user interface.

## Live Demo

To see the Loan Prediction System in action, you can try out the live demo. Click the link below to interact with the application and test different loan application scenarios:

[**Live Demo of Loan Prediction System**](https://loan-prediction-9lu3rck7u7ytz8wpzxgugv.streamlit.app/)

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
