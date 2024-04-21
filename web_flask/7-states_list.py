#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
/states_list: Displays an HTML page: (inside the tag BODY)
    H1 tag: 'States"
    UL tag: List of all State objects in DBStorage sorted by name (A->Z)
        LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with the states listed in alphabetical order
    """

    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def db_teardown(exception):
    """
    Close DB_Storage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
