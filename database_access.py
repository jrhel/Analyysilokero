import sqlite3

def get_connection():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

def verify_database():
    user_table = "CREATE TABLE IF NOT EXISTS User (id integer PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)"
    database = get_connection()
    database.execute(user_table)
    database.commit()
    database.close()

def create_account(username: str, password_hash: str):
    verify_database()
    database = get_connection()
    values = f"'{username}', '{password_hash}'"
    database.execute(f"INSERT INTO User (username, password_hash) VALUES ({values})")
    database.commit()
    database.close()

def query_database(query: str):
    verify_database()
    database = get_connection()
    result = database.execute(query).fetchall()
    database.close()
    return result[0]['username']