import os
from flask import Flask, jsonify, request

app = Flask(__name__)

SENSITIVE_INFO = {
    "Username": "admin123",
    "password": "supersecretadminpassword",
    "address": "secretaddress 123",
    "SSN": "1337123414"
}

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set!")

def is_key():
    return request.headers.get("X-API-key") == API_KEY

@app.get("/data")
def data():
    if not is_key():
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(SENSITIVE_INFO)

if __name__ == "__main__":
    print("API_KEY =", API_KEY)
    app.run(host="127.0.0.1", port=3000)

## Copy this code in new terminal to enter the server
##curl.exe -H "X-API-key: pass123" http://127.0.0.1:3000/data
