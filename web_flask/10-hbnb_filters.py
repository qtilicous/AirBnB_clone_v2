#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
    """Display HBNB filters"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()

    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_cities = sorted(cities, key=lambda city: city.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           cities=sorted_cities,
                           amenities=sorted_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
