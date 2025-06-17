# simple flask app

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from gha-test-py! (updated)</h1>'


def greet(name):
    return f"Howsit, {name}!"


def add_one(x):
    return x + 1
