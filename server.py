import os

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Python microservice called."


@app.route("/test")
def test():
    return "Python ms test endpoint called."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', 3000))
