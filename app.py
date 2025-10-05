from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import db_connection_handler
import logic

app = Flask(__name__)
app.secret_key = "17fa24cf6a2ad4dac44a43963dd2c43e"
logic.initialize_logic()

@app.route("/")
def index():
    if "username" in session.keys():
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

@app.route("/sign_out", methods=["POST"])
def sign_out():
    session.clear()
    # del session["username"]
    return redirect("/")

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
    if logic.create_user(username, password1):
        session["username"] = username
        return redirect("/user_page")
    else:
        return "Successfull sign-up could not be verified from the database."

@app.route("/user_page")
def user_page():
    if "question" in session:
        del session["question"]
    return render_template("user_page/index.html")

@app.route("/analysis", methods=["POST"])
def analysis():
    known_hypotheses = []
    if "known_hypotheses" in session.keys():
        known_hypotheses = session["known_hypotheses"]
    return render_template("analysis/index.html", hypotheses=known_hypotheses)

@app.route("/new_question", methods=["POST"])
def new_analysis():
    question = request.form["new_question"]
    logic.create_analysis(question, session["username"])
    session["question"] = question
    return redirect("/analysis", code=307)

@app.route("/update_analysis", methods=["POST"])
def update_analysis():
    new_question = request.form["update_analysis"]
    if logic.update_analysis(session["question"], new_question, session["username"]):
        session["question"] = new_question
    return redirect("/analysis", code=307)

@app.route("/new_hypothesis", methods=["POST"])
def new_hypothesis():
    new_hypothesis = request.form["new_hypothesis"]
    if logic.set_hypothesis(new_hypothesis, session["question"], session["username"]):

        if "known_hypotheses" in session.keys():
            known_hypotheses = session["known_hypotheses"]
            known_hypotheses.append(new_hypothesis)
            session["known_hypotheses"] = known_hypotheses
        else:
            session["known_hypotheses"] = [new_hypothesis]
            
    # analysis_id = db_connection_handler.get_value("Analysis", "id")
    # values = f"'{new_hypothesis}', '{str(analysis_id)}'"
    # db_connection_handler.insert("Hypothesis", "claim, analysis_id", values)
    
    return redirect("/analysis", code=307)


