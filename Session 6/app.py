from flask import Flask,render_template,url_for
from employee import employee_data

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

@app.route('/employee')
def employee():
    return render_template('employee.html',title='Employee',emps=employee_data)

@app.route('/intern')
def intern():
    return render_template('intern.html',title='Interns',emps=employee_data)

if __name__ == '__main__':
    app.run(debug=True)