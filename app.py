"""
Module with a simple Flask application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Return a simple HTML page.

    Returns:
    -------
    str
        HTML content to be displayed.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
