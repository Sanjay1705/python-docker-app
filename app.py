from flask import Flask, jsonify
import os

app = Flask(__name__)

GREETING = os.getenv("APP_GREETING", "Hello from Dockerized Python App!")

@app.route("/")
def home():
    return GREETING

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
