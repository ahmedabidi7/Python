from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def playd():
    return render_template("index.html", phrase="blue", times=int(3))

@app.route("/play/<x>")
def playb(x):
    return render_template("index.html", phrase="blue", times=int(x))

@app.route("/play/<x>/<color>")
def play(x,color):
    return render_template("index.html", phrase=color, times=int(x))



if __name__=="__main__":
    app.run(debug=True)
