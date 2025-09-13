from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # allow all origins

TELEGRAM_API = "https://api.telegram.org/bot{token}/{method}"

@app.route("/telegram/<token>/<method>", methods=["GET", "POST"])
def proxy(token, method):
    url = TELEGRAM_API.format(token=token, method=method)
    if request.method == "GET":
        r = requests.get(url, params=request.args)
    else:  # POST
        r = requests.post(url, json=request.get_json(force=True))
    return jsonify(r.json())
