#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_db(close_db):
    """Closes db session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display HTML page with list of states """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())

if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
