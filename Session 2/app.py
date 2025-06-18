from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "<h1>This is first page</h1>"

@app.route("/home")
def home():
    return "<h1>This is home page</h1>"

@app.route("/add/<int:n1>/<int:n2>")
def add(n1,n2):
    return f"<h1>Their addition is {n1+n2}</h1>"

@app.route("/welcome/pratik")
def welcome():
    return "<h1>This is Pratik's welcome page</h1>"

@app.route("/welcome/kumar")
def welcome1():
    return "<h1>This is kumar's welcome page</h1>"

@app.route("/welcome/<name>")
def welcome2(name):
    return f"<h1>This is {name}'sd welcome page</h1>"




if __name__ == "__main__":
    app.run(debug=True)