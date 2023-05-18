from flask import Flask, render_template
app = Flask(__name__)




@app.route("/play/<x>/<color>")
def play(x,color):
    return render_template("index.html", phrase=color, times=int(x))



@app.route("/say/<name>")
def hello_name(name):
    return "Hi "+name+"!"

if __name__=="__main__":
    app.run(debug=True)
