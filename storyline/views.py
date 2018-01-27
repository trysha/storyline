#!/usr/bin/python
"""
Views for Storyline
"""
from . import app


@app.route('/')
def root():
    """
    A happy little index
    """
    return 'Hello World!'
