import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("data/login_logs.csv")

# Feature engineering
df["hour"] = pd.to_datetime(df["login_time"], format="%H:%M").dt.hour

# Encode categorical features
geo_encoder = LabelEncoder()
df["geo_encoded"] = geo_encoder.fit_transform(df["ip_address"])

method_encoder = LabelEncoder()
df["method_encoded"] = method_encoder.fit_transform(df["login_method"])

# Define feature matrix and target — use fixed column order
feature_order = ["failed_attempts", "hour", "geo_encoded", "method_encoded"]
X = df[feature_order]
y = df["is_threat"]

# Save feature order
joblib.dump(feature_order, "feature_order.pkl")

# Train and save model
model = XGBClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
joblib.dump(geo_encoder, "geo_encoder.pkl")
joblib.dump(method_encoder, "method_encoder.pkl")