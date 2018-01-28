#!/usr/bin/python
"""
access the storyline database
"""
import sqlite3


class StoryDB(object):
    """
    Search The storyline Database
    """
    def __init__(self, database, g) -> None:
        self.database = database
        self.flask_g = g

    def get(self, story_id) -> dict:
        """ get a story """
        print("GET %s" % (story_id))
        return {'storyid': story_id}

    def delete(self, story_id) -> bool:
        """ delete a story """
        print("DELETE %s" % (story_id))
        return False

    def update(self, story_id=None) -> str:
        """ create or update a story """
        print("UPDATE %s" % (story_id))
        return None

    def search(self, query) -> list:
        """ search the database """
        print("SEARCHING")
        return []

    def connect_db(self):
        """Connects to the storyline database."""
        result = sqlite3.connect(self.database)
        result.row_factory = sqlite3.Row
        return result

    def get_db(self):
        """Opens a new database connection if there is none yet for the current
        application context.
        """
        if not hasattr(self.flask_g, 'sqlite_db'):
            self.flask_g.sqlite_db = self.connect_db()
        return self.flask_g.sqlite_db

    def close_db(self):
        """Closes the database again at the end of the request."""
        if hasattr(self.flask_g, 'sqlite_db'):
            self.flask_g.sqlite_db.close()
