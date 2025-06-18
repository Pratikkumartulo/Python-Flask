from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hey everyone, this is home page</h1>"

@app.route("/about")
def about():
    return "<h1>Hey everyone, this is about page</h1>"

@app.route("/login")
def login():
    return "<div>Login page<br><input type='email' placeholder='email here'/><br><input type='password' placeholder='password here'/><br><button>Submit</button>" \
    "</div>"

@app.route("/welcome/<name>/<name2>")
def welcome(name,name2):
    return f"<h3>Welcome ,{name} and {name2}</h3>"

@app.route("/add/<int:n1>/<int:n2>")
def add(n1,n2):
    return f"<h5>Their addition is {n1+n2}</h5>"

@app.route("/welcomeagain/<name>")
def welcomeagain(name):
    titled_name = name.title()
    return f"<h2>Welcome, {titled_name}"

if __name__ == "__main__":
    app.run(debug=True)