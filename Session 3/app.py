from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/pass')
def passed():
    return '<h1>Congrats you are passed !!</h1>'

@app.route('/fail')
def failed():
    return '<h1>Sorry you are failed !!</h1>'

@app.route('/marks/<int:mark>')
def marks(mark):
    if mark < 30:
        return redirect(url_for('failed'))
    else:
        return redirect(url_for('passed'))


if __name__ == '__main__':
    app.run(debug=True)