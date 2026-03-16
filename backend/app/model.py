# ======================================
# Import Libraries
# ======================================

import pickle
import pandas as pd


# ======================================
# Load Saved Model and Scaler
# ======================================

with open("../churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("../scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


# ======================================
# Numerical Columns Used in Scaling
# ======================================

num_cols = [
    "creditscore",
    "age",
    "tenure",
    "balance",
    "num_of_products",
    "estimated_salary"
]


# ======================================
# Prediction Function
# ======================================

def predict_churn(features_dict):

    # Convert dictionary input to DataFrame
    df = pd.DataFrame([features_dict])

    # Apply scaling to numerical columns
    df[num_cols] = scaler.transform(df[num_cols])

    # Generate prediction
    prediction = model.predict(df)[0]

    # Return prediction as integer
    return int(prediction)
