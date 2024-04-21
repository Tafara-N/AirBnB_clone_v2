#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C ", then value of the text variable
    /python/(<text>): Displays "Python ", then value of the text variable
        :Default value of text is "is cool"
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
        HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Displays:
        "C ", then the value of the text variable
    """
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Displays:
        "Python ", then the value of the text variable
    """

    return "Python " + text.replace("_", " ")
