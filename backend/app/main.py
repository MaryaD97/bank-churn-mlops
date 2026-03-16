# ======================================
# FastAPI Backend for Bank Churn Model
# ======================================

from fastapi import FastAPI
from pydantic import BaseModel

from app.model import predict_churn


# ======================================
# Initialize FastAPI App
# ======================================

app = FastAPI(
    title="Bank Churn Prediction API",
    description="API for predicting customer churn using a trained ML model",
    version="1.0"
)


# ======================================
# Define Input Data Schema
# ======================================

class CustomerFeatures(BaseModel):

    creditscore: float
    age: float
    tenure: float
    balance: float
    num_of_products: float
    estimated_salary: float

    has_credit_card: int
    is_active_member: int

    geography_germany: int
    geography_spain: int

    gender_male: int


# ======================================
# Root Route
# ======================================

@app.get("/")
def home():
    return {"message": "Bank Churn Prediction API is running"}


# ======================================
# Prediction Route
# ======================================

@app.post("/predict")
def predict(data: CustomerFeatures):

    # Convert input object to dictionary
    input_dict = data.dict()

    # Call ML model
    prediction = predict_churn(input_dict)

    return {
        "churn_prediction": prediction
    }
  
