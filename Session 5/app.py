from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>For calculator use /num1/num2 route</h1>"

@app.route('/<int:num1>/<int:num2>')
def home(num1,num2):
    return render_template('home.html',num1=num1,num2=num2)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return render_template('addition.html',title="Addition", num1=num1, num2=num2,sum=num1 + num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return render_template('substraction.html',title="Subtraction", num1=num1, num2=num2,diff=num1 - num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):   
    return render_template('multiply.html',title="Multiplication", num1=num1, num2=num2,prod=num1 * num2)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):  
    if num2 == 0:
        return render_template('division.html', title="Division", num1=num1, num2=num2, divi="",error="Division by zero is not allowed !!")
    return render_template('division.html', title="Division", num1=num1, num2=num2, divi=num1 / num2)

if __name__ == '__main__':
    app.run(debug=True)