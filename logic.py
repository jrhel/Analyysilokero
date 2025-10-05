from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import userDAO
import analysisDAO
import hyphotesisDAO
import db_connection_handler

def initialize_logic():
    db_connection_handler.verify_database()

# Sends information about new user to userDAO to be saved.
# Returns True if saved username maches intended, else False.
def create_user(username: str, password: str):
    print("Logic: Create account for: username")
    password_hash = generate_password_hash(password)
    if userDAO.create_user(username, password_hash) == username:
        print("Logic: Created account for:", username)
        return True
    else:
        print("Logic: Failed to create account for:", username)
        return False

# Sends information about new analysis to analysisDAO to be saved.
def create_analysis(question: str, username: str):
    print("Logic: Creating new analysis:", question, "for", username)
    analysisDAO.create_analysis(question, username)
    print("Logic: Analysis should now exist.")

# Sends a question to be updated to a new one for a specific user.
# Returns True if saved question maches new intended one, else False.
def update_analysis(old_question: str, new_question: str, username: str):
    print("Logic: Update", old_question, "TO", new_question, "FOR", username)
    if analysisDAO.update_question(old_question, new_question, username) == new_question:
        return True
    else: 
        return False

def set_hypothesis(new_hypothesis: str, question: str, username: str):
    admin_id = userDAO.get_user("username", username)[0]
    analysis_id = analysisDAO.get_pk(question, admin_id)
    return hyphotesisDAO.create_hypothesis(new_hypothesis, analysis_id)
