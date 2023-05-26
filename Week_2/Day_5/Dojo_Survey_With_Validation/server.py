from flask import Flask, render_template, request, redirect, session
import random
from user_model import User

app = Flask(__name__)
app.secret_key = "akounamatata"

@app.route("/")
def indexf():
    return render_template("index.html")

@app.route("/check", methods=['POST'])
def check():
    if not User.validate(request.form):
        return redirect("/")
    User.create(request.form)
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect("/result")

@app.route("/result")
def resultpage():
    return render_template("result.html")

@app.route("/reset")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
