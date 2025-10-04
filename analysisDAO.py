import db_connection_handler
import userDAO

def create_analysis(question: str, username: str):
    print("AnalysisDAO: Creating new analysis...")
    user_id = userDAO.get_user("username", username)[0]
    params = [question, user_id]
    if db_connection_handler.execute("INSERT INTO Analysis (question, admin) VALUES (?, ?)", params) == "-1":
        print("AnalysisDAO: Creation of new analysis seems to have failed.")
        return False
    else:
        print("AnalysisDAO: Analysis created  successfully!")
        return True
    
def update_question(old_question: str, new_question: str, username: str):
    admin_id = userDAO.get_user("username", username)[0]
    params =[new_question, old_question, admin_id]
    pk = get_question_pk(old_question, admin_id)
    db_connection_handler.execute("UPDATE Analysis SET question = ? WHERE question = ? AND admin = ?", params)
    return_value = get_question(pk)[1]
    print("RETUR_VALUE:", return_value)
    return return_value

def get_question(id):
    question_info = "No such question"
    params = [id]
    result = db_connection_handler.query("SELECT * FROM Analysis WHERE id = ?", params)
    print("GET_QUESTION_result:", result)
    question_info = result[0]
    print("GET_QUESTION_info:", question_info)
    return question_info

def get_question_pk(question: str, admin_id: int):
    params = [question, admin_id]
    pk = db_connection_handler.query("SELECT * FROM Analysis WHERE question = ? AND admin = ?", params)[0][0]
    return pk
