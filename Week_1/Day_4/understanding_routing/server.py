from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def hello_dojo():
    return "Dojo!"

@app.route("/say/<name>")
def hello_name(name):
    return "Hi "+name+"!"

@app.route("/repeat/<x>/<word>")
def repeat_word(x,word):
    return (word+"<br>")*int(x)


if __name__=="__main__":
    app.run(debug=True)