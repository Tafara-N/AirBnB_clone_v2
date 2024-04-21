#!/usr/bin/python3

"""
Script starts Flask web app, listens on `0.0.0.0:5000` with route:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C ", then value of the text variable
    /python/(<text>): Displays "Python ", then value of the text variable
        :Default value of text is "is cool"
    /number/<n>: Displays "n is a number" Only if `n` is an int
    /number_template/<n>: Displays an HTML page only if `n` is an int
        :H1 tag: "Number: n" inside the tag BODY
    /number_odd_or_even/<n>: Displays an HTML page only if `n` is an int
        :H1 tag: "Number: n is even|odd" inside the tag BODY
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def im_a_number(n):
    """
    Displays:
        "n is a number" Only if `n` is an int
    """

    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbers_and_templates(n):
    """
    Displays an HTML page only if `n` is an int
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numbers_and_evenness(n):
    """
    Displays an HTML page only if `n` is an int
    """
    if n % 2 == 0:
        evenness = "even"
    else:
        evenness = "odd"
    return render_template(
        "6-number_odd_or_even.html", n=n, evenness=evenness)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
