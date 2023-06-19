#!/usr/bin/python3
"""This script starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return render_template("10-hbnb_filters.html")

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=None)
