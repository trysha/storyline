#!/usr/bin/python
"""
Views for Storyline
"""
from flask import jsonify, render_template
from . import app, story_db


@app.route('/')
def root():
    """
    A happy little index
    """
    return render_template("page.html")


@app.route("/api/v1/story/<int:storyid>", methods=['GET'])
def story_get(storyid):
    """
    get a story
    """
    return jsonify(story_db.get(storyid))


@app.route("/api/v1/story/<int:storyid>", methods=['DELETE'])
def story_delete(storyid):
    """
    delete a story
    """
    return jsonify(story_db.delete(storyid))


@app.route("/api/v1/story", methods=['PUT', 'POST'])
def story_update():
    """
    update/create a story
    """
    return jsonify(story_db.update())
