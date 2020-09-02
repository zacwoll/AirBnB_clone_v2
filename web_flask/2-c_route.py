#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print a hello """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print 'HBNB' """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Print C <text> """
    return 'C {}'.format(text).replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
