from flask import Flask, request, abort


app = Flask(__name__)

valid_endpoints = ['hello world', 'hello', 'world']

@app.route('/', defaults={'word': 'hello world'})
@app.route('/<word>')
def hello_world(word):
    if word not in valid_endpoints:
        abort(404)

    if 'uppercase' in request.args:
        word = word.upper()

    if 'reversed' in request.args:
        word = word[::-1]

    return word
