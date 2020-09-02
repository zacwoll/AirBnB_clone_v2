#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_db(close_db):
    """ Closes db session """
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def get_states(id='0'):
    """ Display HTML page with list of states """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(), id=id)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
