import db_connection_handler

# Forms SQL-statements & parameters to be submitted to the db_connection_handler,
# & returns the username as saved in the database.
def create_user(username: str, password_hash: str):
    print("UserDAO: Create account for:", username)
    params = [username, password_hash]
    id = db_connection_handler.execute("INSERT INTO User (username, password_hash) VALUES (?, ?)", params)
    print("UserDAO: Result:", get_user("id", id))
    return get_user("id", id)[1]

# Queries the db_connection_handler for user information based on column specific value in "User"-table in database
def get_user(column: str, value: str):
    user_info = "No such user"
    params = [value]
    if column == "id":
        result = db_connection_handler.query("SELECT * FROM User WHERE id = ?", params)
        user_info = result[0]
    elif column == "username":
        result = db_connection_handler.query("SELECT * FROM User WHERE username = ?", params)
        user_info = result[0]
    return user_info