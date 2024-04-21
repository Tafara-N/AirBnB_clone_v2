#!/usr/bin/python3

"""
/hbnb_filters: Displays an HTML page like 6-index.html
    :State, City and Amenity objects loaded from DBStorage and
    sorted by name (A->Z)
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """
    Displays an HTML page from 'static'
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities
        )


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the DB_Storage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
