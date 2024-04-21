#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
/states: display a HTML page: (inside the tag BODY)
    :H1 tag: "States"
    :UL tag: List all State objects present in DBStorage sorted by name (A->Z)
        :LI tag: Description of one State: <state.id>: <B><state.name></B>

/states/<id>: Displays a HTML page: (inside the tag BODY)
If a State object is found with this id:
    :H1 tag: "State: "
    :H3 tag: "Cities:"
    :UL tag: with the list of City objects linked to the State sorted by name (A->Z)
        :LI tag: description of one City: <city.id>: <B><city.name></B>
    :Otherwise:
        :H1 tag: “Not found!”
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays States and Cities listed in alphabetical order
    """

    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the DB_Storage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
