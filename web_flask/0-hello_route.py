#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000`
with route '/' displaying "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Returns:
        "Hello HBNB!"
    """

    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
