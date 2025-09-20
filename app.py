from flask import Flask
from flask import render_template
from flask import request
from werkzeug.security import generate_password_hash
import database_access

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/sign_in")
def page1():
    
    return render_template("sign_in/index.html")

@app.route("/sign_up")
def page2():

    return render_template("sign_up/index.html")

@app.route("/create_account", methods=["POST"])
def page3():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:        
        return "Salasanat eivät täsmää!"
    password_hash = generate_password_hash(password1)
    database_access.create_account(username, password_hash)
    result = database_access.query_database(f"SELECT username FROM User WHERE password_hash = '{password_hash}'")
    if result == username:
        return f"Tervetuloa {username}! Tunnuksen luominen onnistui.
    else:
        return "Successfull sign-up could not be verified from the database."


