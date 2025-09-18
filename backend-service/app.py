from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend running"})

@app.route("/auth")
def call_auth():
    return {"auth": "Auth service placeholder"}

@app.route("/payments")
def call_payments():
    return {"payments": "Payments service placeholder"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
