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
    return 'Hello HBNB!'


# Define a route for the '/hbnb' endpoint that displays "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Define a route for the '/c/<text>' endpoint that displays "C <text>"
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(escape(text).replace('_', ' '))


# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
