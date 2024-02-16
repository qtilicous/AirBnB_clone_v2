#!/usr/bin/python3
"""
A Flask web application with routes for displaying messages.
"""

from flask import Flask, escape

# Create an instance of the Flask application
app = Flask(__name__)


# Define a route for the root URL '/' that displays "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when the root URL is accessed.
    """
    return 'Hello HBNB!'


# Define a route for the '/hbnb' endpoint that displays "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when the '/hbnb' endpoint is accessed.
    """
    return 'HBNB'


# Define a route for the '/c/<text>' endpoint that displays "C <text>"
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C <text>" when the '/c/<text>' endpoint is accessed.
    Replace underscores (_) in <text> with spaces.
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


# A route for the '/python/<text>' endpoint that displays "Python <text>"
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display "Python <text>" when the '/python/<text>' endpoint is accessed.
    If no text is provided, use the default value "is cool".
    Replace underscores (_) in <text> with spaces.
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))


# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
