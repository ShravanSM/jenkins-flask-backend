
import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Status Dashboard",
        "service": "Flask Backend",
        "version": APP_VERSION,
        "message": "Flask backend is running!",
        "status": "UP"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-backend"
    }), 200


@app.route("/api/status")
def status():
    return jsonify({
        "application": "DevOps Status Dashboard",
        "backend": "Flask",
        "status": "UP",
        "version": APP_VERSION
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
