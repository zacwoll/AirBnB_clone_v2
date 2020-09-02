#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def _python(text="is cool"):
    """ Print python <text> """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def get_num(n):
    """ Return n if it is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def get_num_template(n):
    """ Display an HTML page if n is number """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def get_num_odd_or_even(n):
    """ Display odd or even if n is a number """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
