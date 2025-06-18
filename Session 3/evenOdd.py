from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>This is landing page</h1>'

@app.route("/even")
def even():
    return '<h1>This is even number</h1>'

@app.route('/odd')
def odd():
    return '<h1>This is odd number</h1>'

@app.route("/num/<int:n>")
def number(n):
    if n%2==0:
        return redirect(url_for('even'))
    else:
        return redirect(url_for('odd'))

if __name__ == "__main__":
    app.run(debug=True)