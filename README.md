# Bank Churn Prediction System

## Overview
This project is a production-style machine learning application that predicts customer churn using a trained classification model. It consists of a FastAPI backend for model inference and a Streamlit frontend for user interaction.

---

## Project Structure

bank-churn-mlops/

├── backend/  
│   └── app/  
│       ├── main.py  
│       ├── model.py  
│       └── churn_model.pkl  

├── frontend/  
│   ├── app.py  
│   └── requirements.txt  

└── README.md  

---

## How to Run the Project

### 1. Run Backend (FastAPI)

Navigate to backend folder:

cd backend  

Start server:

uvicorn app.main:app --reload  

Backend will run on:  
http://127.0.0.1:8000  

---

### 2. Run Frontend (Streamlit)

Open a new terminal and navigate to frontend:

cd frontend  

Run app:

streamlit run app.py  

Frontend will run on:  
http://localhost:8501  

---

## API Usage

### Endpoint  
POST /predict  

### Example Input

{
  "creditscore": 650,
  "age": 40,
  "tenure": 5,
  "balance": 60000,
  "num_of_products": 2,
  "has_credit_card": 1,
  "is_active_member": 1,
  "estimated_salary": 70000,
  "geography_germany": 0,
  "geography_spain": 1,
  "gender_male": 1
}

### Example Output

{
  "churn_prediction": 0
}

- 0 → Customer likely to stay  
- 1 → Customer likely to churn  

---

## Assumptions & Preprocessing

- Input features must match the trained model schema  
- Categorical variables are manually encoded:
  - Geography → Germany, Spain (one-hot encoding)
  - Gender → Male (binary encoding)
- Feature names from API are mapped internally to match model training format  
- Column order is strictly enforced before prediction  
- Model is loaded from a serialized `.pkl` file using pickle  

---

## Tech Stack

- Backend: FastAPI  
- Frontend: Streamlit  
- Machine Learning: Scikit-learn  
- Language: Python  

---

## Notes

- Ensure backend is running before using frontend  
- Localhost URLs are not publicly accessible without deployment  
- For production use, deploy backend and frontend separately  

