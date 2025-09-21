import sqlite3

def get_connection():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

def verify_database():
    user_table = "CREATE TABLE IF NOT EXISTS User (id integer PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)"
    analysis_table = "CREATE TABLE IF NOT EXISTS Analysis (id integer PRIMARY KEY, question TEXT)"
    hypothesis_table = "CREATE TABLE IF NOT EXISTS Hypothesis (id integer PRIMARY KEY, claim TEXT, analysis_id integer,  FOREIGN KEY (analysis_id) REFERENCES Analysis(id))"
    analysis_user_table = "CREATE TABLE IF NOT EXISTS Analysis_User (id integer PRIMARY KEY, user_id integer, analysis_id integer, FOREIGN KEY (user_id) REFERENCES User(id), FOREIGN KEY (analysis_id) REFERENCES Analysis(id))"
    database = get_connection()
    database.execute(user_table)
    database.execute(analysis_table)
    database.execute(hypothesis_table)
    database.execute(analysis_user_table)
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

def get_password_hash(username: str):
    verify_database()
    database = get_connection()
    result = database.execute(f"SELECT password_hash FROM User WHERE username = '{username}'").fetchall()
    database.close()
    return result[0]['password_hash']

def insert(table: str, columns: str, values: str):
    verify_database()
    database = get_connection()
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    print("QUERY =", query)
    database.execute(query)
    print("INSERTED")
    database.commit()
    database.close()

def get_value(table: str, column: str):
    verify_database()
    database = get_connection()
    result = database.execute(f"SELECT {column} FROM {table}").fetchall()
    database.close()
    return result[0][column]