import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect("threats.db")
cursor = conn.cursor()

# Create the threats table
cursor.execute("""
CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,              -- When the threat was detected
    ip TEXT,                     -- IP address of the login attempt
    method TEXT,                 -- Login method used (e.g. SSH, API)
    hour INTEGER,                -- Hour of login attempt
    failed_attempts INTEGER,     -- Number of failed login attempts
    is_threat INTEGER,           -- 1 if flagged as threat, 0 otherwise
    confidence REAL              -- Model's confidence score for threat
)
""")

# Save and close
conn.commit()
conn.close()