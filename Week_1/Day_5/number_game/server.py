from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "akounamatata"

@app.route("/")
def indexf():
    if 'ran' not in session:
        session['ran']=random.randint(1, 100)
    if 'choice' not in session:
        session['choice']=0
    return render_template("index.html")

@app.route("/check", methods=['POST'])
def check():
    session['choice']=int(request.form['guess'])

    return redirect("/")

@app.route("/reset")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
