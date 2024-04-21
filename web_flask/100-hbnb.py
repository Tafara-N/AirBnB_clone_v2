#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
/hbnb: Displays an HTML page like 8-index.html
    :State, City and Amenity objects loaded from DBStorage and
    sorted by name (A->Z)
"""

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def filters():
    """
    Displays an HTML page from 'static'
    """

    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")
    return render_template(
        "100-hbnb.html",
        amenities=amenities,
        places=places,
        states=states
        )


@app.teardown_appcontext
def teardown_db(excpt=None):
    """
    Closes DB_Storage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
