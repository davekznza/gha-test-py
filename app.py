# simple flask app

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to gha-test-py! test</h1>'


def greet(name):
    return f"Howsit, {name}!"


def add_one(x):
    return x + 1
