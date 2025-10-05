import db_connection_handler
import userDAO

def create_analysis(question: str, username: str):
    user_id = userDAO.get_user("username", username)[0]
    params = [question, user_id]
    if db_connection_handler.execute("INSERT INTO Analysis (question, admin) VALUES (?, ?)", params) > 0:
        return True
    else:
        return False
    
# Updates a question for a specific user & returns saved question after update
def update_question(old_question: str, new_question: str, username: str):
    admin_id = userDAO.get_user("username", username)[0]    
    pk = get_pk(old_question, admin_id)
    params = [new_question, old_question, admin_id]
    db_connection_handler.execute("UPDATE Analysis SET question = ? WHERE question = ? AND admin = ?", params)
    return_value = get_question(pk)[1]
    return return_value

def get_question(id):
    question_info = "No such question"
    params = [id]
    result = db_connection_handler.query("SELECT * FROM Analysis WHERE id = ?", params)
    question_info = result[0]
    return question_info

def get_pk(question: str, admin_id: int):
    params = [question, admin_id]
    pk = db_connection_handler.query("SELECT * FROM Analysis WHERE question = ? AND admin = ?", params)[0][0]
    return pk
