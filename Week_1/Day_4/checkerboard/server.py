from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def playd():
    return render_template("index.html", color1="red",color2="black", l=int(8), h=int(8))

@app.route("/<h>")
def playb(h):
    return render_template("index.html", color1="red",color2="black", l=int(h), h=int(8))

@app.route("/<h>/<l>")
def playh(h,l):
    return render_template("index.html", color1="red",color2="black", l=int(h), h=int(l))

@app.route("/<h>/<l>/<c1>")
def playx(h,l,c1):
    return render_template("index.html", color1=c1,color2="black", l=int(h), h=int(l))

@app.route("/<h>/<l>/<c1>/<c2>")
def playy(h,l,c1,c2):
    return render_template("index.html", color1=c1,color2=c2, l=int(h), h=int(l))

if __name__=="__main__":
    app.run(debug=True)
