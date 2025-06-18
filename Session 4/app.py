from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route('/pass/<sname>/<int:smark>')
def passed(sname, smark):
    return f'<h1>Congrats {sname}, you are passed with {smark} marks !!</h1>'

@app.route('/fail/<sname>/<int:smark>')
def failed(sname, smark):
    return f'<h1>Sorry {sname}, you are failed with {smark} marks !!</h1>'

@app.route('/score/<name>/<int:mark>')
def score(name, mark):
    if mark < 30:
        return redirect(url_for('failed', sname =name,smark=mark))
    else:
        return redirect(url_for('passed', sname =name,smark=mark))

if __name__ == '__main__':
    app.run(debug=True)