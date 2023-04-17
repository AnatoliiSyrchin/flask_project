from flask import Flask, request, g

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'
