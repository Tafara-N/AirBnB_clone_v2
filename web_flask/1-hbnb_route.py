#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns:
        "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns:
        "HBNB"
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
