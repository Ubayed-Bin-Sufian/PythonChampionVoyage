# Practice from https://www.youtube.com/watch?v=f085KDOy43k

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"


if __name__=="__main__":
    app.run(debug=True)