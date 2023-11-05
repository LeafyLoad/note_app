"""
Module to work with database
Functions:
Add new note to database
Get all notes from database
Delete note from database
Find a note by search query
"""
import sqlite3
from typing import Union


class DataBase:
    """
    Database class, object have a connection with sqlite database
    """
    def __init__(self):
        self.connection = sqlite3.connect('notedb.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        """
        Function for creating notes table
        Call this function when creating class object
        :return:
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "note_title TEXT UNIQUE,"
                            "note_text TEXT);")
        self.connection.commit()

    def add_note(self, note_title: str, note_text: str) -> bool:
        """
        Function for add new note in note table
        :param note_title:
        :param note_text:
        :return:
        """
        try:
            self.cursor.execute("INSERT INTO notes(note_title, note_text) "
                                "VALUES(?, ?)", (note_title, note_text))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            self.connection.rollback()
            return False

    def delete_note(self, note_id: int) -> None:
        """
        Function for delete note by id
        :param note_id:
        :return:
        """
        self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id, ))
        self.connection.commit()

    def get_all_notes(self) -> list:
        """
        Function for get all notes from table note
        :return:
        """
        self.cursor.execute("SELECT id, note_title FROM notes ORDER BY id")
        return self.cursor.fetchall()

    def search_note_by_query(self, search_query: str) -> Union[list, None]:
        """
        Function for find note by search query
        Search starts from note title, if no search results
        :param search_query:
        :return:
        """
        self.cursor.execute("SELECT * FROM notes WHERE note_title "
                            "LIKE '%' || ? || '%'", (search_query,))
        results = self.cursor.fetchall()
        if not results:
            self.cursor.execute("SELECT * FROM notes WHERE note_text "
                                "LIKE '%' || ? || '%'", (search_query,))
            results = self.cursor.fetchall()
        if not results:
            return None
        return results
