# SOC Pipeline: Modular Threat Detection & IOC intelligence 

A production-ready, modular Security Operations Center (SOC) pipeline that detects suspicious login activity, enriches IPs with threat intelligence from multiple sources, and visualizes results in a real-time dashboard. Built for maintainability, analyst usability, and employer-facing clarity

# Features of the SOC Pipeline 

- 🔍 Threat Detection: ML-based classification of login attempts using XGBoost
- 🌐 IOC Enrichment: Integrates AbuseIPDB and VirusTotal for IP reputation checks
- 📊 Streamlit Dashboard: Analyst-friendly interface with filters, metrics, and IOC visibility
- ⚙️ FastAPI Backend: RESTful endpoints for real-time predictions and threat logging
- 🧠 Model Retraining: Modular hooks for updating and evaluating the detection model
- 🗃️ SQLite Storage: Lightweight, persistent threat event logging


# How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Start the API: `uvicorn main:app --reload`
3. Launch the dashboard: `streamlit run dashboard.py`

# Technologies Used

Python, pandas, FastAPI, Streamlit, SQLite, joblib, XGBoost

# Author

CanUdigit12 — building real-world SOC tools with clarity, modularity, and public documentation.
