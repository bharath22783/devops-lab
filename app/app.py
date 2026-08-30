from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Lab API v1.1 is running\n"

@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "postgres"),
            database=os.getenv("POSTGRES_DB", "labdb"),
            user=os.getenv("POSTGRES_USER", "labuser"),
            password=os.getenv("POSTGRES_PASSWORD", "labpassword")
        )
        conn.close()
        return "healthy\n", 200
    except Exception as e:
        return f"unhealthy: {e}\n", 503

app.run(host="0.0.0.0", port=5000)
