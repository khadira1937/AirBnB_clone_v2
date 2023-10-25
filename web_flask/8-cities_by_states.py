#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities():
        return render_template('8-cities_by_states.html',
                                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
        storage.close()


if __name__ == '__main__':
        app.run(host='0.0.0.0')
