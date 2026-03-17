import streamlit as st
import requests

st.title("Bank Churn Prediction")

st.write("Enter customer details:")

# Inputs
creditscore = st.number_input("Credit Score", value=650)
age = st.number_input("Age", value=40)
tenure = st.number_input("Tenure", value=5)
balance = st.number_input("Balance", value=60000.0)
num_of_products = st.number_input("Number of Products", value=2)
estimated_salary = st.number_input("Estimated Salary", value=70000.0)

has_credit_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

geography = st.selectbox("Geography", ["Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])

# Convert to model format
geography_germany = 1 if geography == "Germany" else 0
geography_spain = 1 if geography == "Spain" else 0
gender_male = 1 if gender == "Male" else 0


# Predict button
if st.button("Predict"):

    data = {
        "creditscore": creditscore,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "num_of_products": num_of_products,
        "has_credit_card": has_credit_card,
        "is_active_member": is_active_member,
        "estimated_salary": estimated_salary,
        "geography_germany": geography_germany,
        "geography_spain": geography_spain,
        "gender_male": gender_male
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        if result["churn_prediction"] == 1:
            st.error("Customer is likely to churn")
        else:
            st.success("Customer is likely to stay")

    except:
        st.error("Error connecting to backend. Make sure FastAPI is running.")
