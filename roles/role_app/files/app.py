#!/usr/bin/env python3
from flask import Flask, jsonify
import os
import socket
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    env = os.environ.get('ENV', 'unknown')
    return f"Hello from {hostname} in {env} environment"

@app.route('/api/mock')
def mock():
    mock_url = os.environ.get('MOCK_URL', 'http://192.168.121.20:5001/mock')
    try:
        r = requests.get(mock_url, timeout=2)
        return jsonify(r.json())
    except:
        return jsonify({"error": "mock service unavailable"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
