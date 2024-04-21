#!/usr/bin/python3

"""
/states: display a HTML page: (inside the tag BODY)
    :H1 tag: "States"
    :UL tag: List of all State objects in DBStorage sorted by name (A->Z)
        :LI tag: Description of one State: <state.id>: <B><state.name></B>

/states/<id>: Displays an HTML page: (inside the tag BODY)
    :If a State object is found with this id:
    :H1 tag: "State: "
    :H3 tag: "Cities:"
    :UL tag: List of City objects linked to the State sorted by name (A->Z)
        :LI tag: description of one City: <city.id>: <B><city.name></B>
    :Otherwise:
        :H1 tag: "Not found!"
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """
    Displays States and Cities listed in alphabetical order
    """

    states = storage.all("State")
    if state_id is not None:
        state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the DB_Sstorage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
