import streamlit as st # lets you tranform python scripts into an interactive web
import pandas as pd
import sqlite3

# Set page config
st.set_page_config(page_title="Threat Detection Dashboard", layout="wide")

# Title
st.title("🚨 Threat Detection Dashboard")

# Connect to SQLite database
conn = sqlite3.connect("threats.db")

# Load recent threats
df = pd.read_sql_query("SELECT * FROM threats ORDER BY timestamp DESC LIMIT 100", conn)

# Show total threats
st.metric("Total Threats Logged", len(df))

# Show raw data table
st.subheader("Recent Threats")
st.dataframe(df)

# Plot threats by hour
st.subheader("Threats by Hour of Day")
hour_counts = df["hour"].value_counts().sort_index()
st.bar_chart(hour_counts)

# Plot confidence scores over time
st.subheader("Confidence Scores Over Time")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df_sorted = df.sort_values("timestamp")
st.line_chart(df_sorted.set_index("timestamp")["confidence"])

# Optional: Group by login method
st.subheader("Threats by Login Method")
method_counts = df["method"].value_counts()
st.bar_chart(method_counts)

# Close DB connection
conn.close()