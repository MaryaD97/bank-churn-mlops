# Bank Churn Prediction ML System

This project demonstrates an end-to-end machine learning pipeline for predicting bank customer churn.

## Project Components

- Data preprocessing and feature engineering
- Machine learning model training (XGBoost)
- Model evaluation and feature importance
- FastAPI backend for model inference
- MLOps-style project structure

## Tech Stack

- Python
- Scikit-learn
- XGBoost
- FastAPI
- Uvicorn

## Project Structure

bank-churn-mlops/
│
├── backend/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── model.py
