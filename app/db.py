import sqlite3

connection = None


def open_db():
    connection = sqlite3.connect(":memory:")


def close_db():
    if connection:
        connection.close()
