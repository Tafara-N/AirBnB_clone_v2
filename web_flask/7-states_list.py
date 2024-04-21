#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
/states_list: Displays an HTML page: (inside the tag BODY)
    :H1 tag: 'States"
    :UL tag: Lists of all State objects in DBStorage sorted by name (A->Z)
        : LI tag: Description of one State: <state.id>: <B><state.name></B> +
        UL tag: Lists of City objects linked to the State sorted by name (A->Z)

            :LI tag: Description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exc):
    """
    Close DB_Storage on teardown
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """
    Displays an HTML page with the states listed in alphabetical order
    """

    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
