import os

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Python microservice called."


@app.route("/test")
def test():
    return "Python ms test endpoint called."


@app.route("/node")
def node():
    node_backend = os.getenv('NODE_BACKEND')
    return requests.get(f"http://{node_backend}").content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', 3000))
