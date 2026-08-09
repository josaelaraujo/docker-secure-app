import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def index():
    env = os.environ.get("APP_ENV", "development")
    return jsonify(message="API rodando", ambiente=env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)