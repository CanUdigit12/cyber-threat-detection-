from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import joblib
import sqlite3

# Initialize FastAPI app
app = FastAPI()

# Load trained model and encoders
model = joblib.load("model.pkl")
geo_encoder = joblib.load("geo_encoder.pkl")
method_encoder = joblib.load("method_encoder.pkl")
feature_order = joblib.load("feature_order.pkl")

# Define input schema for POST requests
class LoginData(BaseModel):
    failed_attempts: int
    ip_address: str
    login_time: str  # Format: "HH:MM"
    login_method: str

# Function to log flagged threats to SQLite database
def log_threat(data, hour, is_threat, confidence):
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO threats (timestamp, ip, method, hour, failed_attempts, is_threat, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),      # Current timestamp
        data.ip_address,                 # IP address from request
        data.login_method,              # Login method used
        hour,                            # Parsed hour from login_time
        data.failed_attempts,            # Number of failed attempts
        int(is_threat),                  # 1 if threat, 0 if normal
        float(confidence)                # Model's confidence score
    ))
    conn.commit()
    conn.close()

# Define prediction endpoint
@app.post("/predict")
def predict(data: LoginData):
    try:
        # Extract hour from login_time
        hour = datetime.strptime(data.login_time, "%H:%M").hour

        # Encode IP address safely (fallback to -1 if unseen)
        geo_encoded = geo_encoder.transform([data.ip_address])[0] if data.ip_address in geo_encoder.classes_ else -1

        # Encode login method safely (fallback to -1 if unseen)
        method_encoded = method_encoder.transform([data.login_method])[0] if data.login_method in method_encoder.classes_ else -1

        # Build input DataFrame for prediction
        X = pd.DataFrame([{
            "failed_attempts": data.failed_attempts,
            "hour": hour,
            "geo_encoded": geo_encoded,
            "method_encoded": method_encoded
        }])
        X = X[feature_order]  # Reorder columns to match training

        # Make prediction and get confidence score
        prediction = model.predict(X)[0]  # 0 or 1
        confidence = model.predict_proba(X)[0][1]  # Probability of class 1 (threat)

        # Log threat to database if flagged
        if prediction == 1:
            log_threat(data, hour, prediction, confidence)

        # Return result to client
        return {
            "is_threat": bool(prediction),
        }

    except Exception as e:
        # Return error if prediction fails
        raise HTTPException(status_code=400, detail=str(e))