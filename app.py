from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/sign_in")
def page1():
    
    return render_template("sign_in/index.html")

@app.route("/create_account")
def page2():

    return render_template("create_account/index.html")


