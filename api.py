from flask import Flask, jsonify

app = Flask(__name__)

SENSITIVE_INFO = {
  "Username" : "admin123",
  "password" : "supersecretadminpassword",
  "address" : "secretaderss 123",
  "SSN" : "1337123414"
}

@app.get('/data')

def data():
  return jsonify(SENSITIVE_INFO)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3000)
