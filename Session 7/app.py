from flask import Flask, flash,render_template,redirect,url_for
from forms import SignupForm, LoginForm

users = {}

app = Flask(__name__)
app.config["SECRET_KEY"] = "15bb914121bfb88e90cd224850b5e614"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="Home")

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email == "pratiktulo42@gmail.com" and password == "12345678" or email in users and users[email]['password'] == password:
            flash('01Login successful!')
            return redirect(url_for('home'))
        else:
            flash('02Imvalid email or password. !!!!')
    return render_template('login.html',title="login",form=form)

@app.route("/signup",methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.email.data in users:
            flash('02Email already exists. Please choose a different one.')
        else:
            users[form.email.data] = {
                'username': form.username.data,
                'password': form.password.data,
                'dob': form.dob.data,
                'gender':form.gender.data
            }
            flash(f'01Signup successful! Welcome {form.username.data}!')
            return redirect(url_for('home'))
    return render_template('signup.html',title="signup",form=form)

if __name__ == "__main__":
    app.run(debug=True)