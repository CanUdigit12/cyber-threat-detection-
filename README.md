# Cyber Threat Detection System 
# Cyber Threat Detection System

This project is a modular SOC pipeline for detecting login-based threats using machine learning. It includes:

-  Data ingestion and logging
-  Threat prediction via XGBoost
-  FastAPI interface for querying predictions
-  Streamlit dashboard for visualization
-  Alerting, retraining, and model evaluation modules

# How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Start the API: `uvicorn main:app --reload`
3. Launch the dashboard: `streamlit run dashboard.py`

# Technologies Used

Python, pandas, FastAPI, Streamlit, SQLite, joblib, XGBoost

# Author

CanUdigit12 — building real-world SOC tools with clarity, modularity, and public documentation.
