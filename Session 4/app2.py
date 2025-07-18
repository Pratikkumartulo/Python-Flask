from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/evaluate/<int:n1>')
def evaluate(n1):
    return render_template('evaluate.html',title='Evaluate',numS=n1)

if __name__ == '__main__':
    app.run(debug=True)