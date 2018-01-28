#!/usr/bin/python
"""
Storyline!
"""
# pylint: disable=C0103,C0413
import os
import sqlite3
# from flask import Flask, request, session, g, redirect, url_for, abort, \
#     render_template, flash
from flask import Flask, g
from .database import StoryDB

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'storyline.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('STORYLINE_SETTINGS', silent=True)

story_db = StoryDB(app.config['DATABASE'], g)


def init_db():
    """ initialize the database, call with python -m storyline -e 'init_db()'
    """
    with app.app_context():
        db = story_db.get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def teardown_appcontext(error):
    """ things to do when app is torn down """
    story_db.close_db()


from . import views
