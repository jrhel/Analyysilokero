import database_access

def create_user(username: str, password_hash: str):
    params = [username, password_hash]
    id = database_access.execute("INSERT INTO User (username, password_hash) VALUES (?, ?)", params)
    get_user(id)

def get_user(id):
    params = [id]
    user_info = database_access.query("SELECT * FROM User WHERE id = ?", params)
    column = 0
    for key in user_info[0]:
        print("Column: ", column, "; Key: ", key)
        column +=1