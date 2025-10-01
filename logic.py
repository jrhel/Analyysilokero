from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import userDAO
import database_access

def initialize_logic():
    database_access.verify_database()

def create_user(username: str, password: str):
    password_hash = generate_password_hash(password)
    userDAO.create_user(username, password_hash)
