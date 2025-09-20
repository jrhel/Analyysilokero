from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import database_access

app = Flask(__name__)
app.secret_key = "17fa24cf6a2ad4dac44a43963dd2c43e"

@app.route("/")
def index():
    if in_session():
        return redirect("/user_page")
    else:
        return render_template("index.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    password_hash = database_access.get_password_hash(username)
    
    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/user_page")
    else:
        return "Sign-in information was incorrect."

@app.route("/sign_up")
def sign_up():

    return render_template("sign_up/index.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:        
        return "Salasanat eivät täsmää!"
    password_hash = generate_password_hash(password1)
    database_access.create_account(username, password_hash)
    result = database_access.query_database(f"SELECT username FROM User WHERE password_hash = '{password_hash}'")
    if result == username:
        session["username"] = username
        return redirect("/user_page")
    else:
        return "Successfull sign-up could not be verified from the database."
    
@app.route("/user_page")
def user_page():
    return render_template("user_page/index.html")

@app.route("/sign_out", methods=["POST"])
def sign_out():
    del session["username"]
    return redirect("/")

def in_session():
    if "username" in session.keys():
        return True
    return False