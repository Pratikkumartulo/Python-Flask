from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,Email,optional,EqualTo

class SignupForm(FlaskForm):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(4,15)],
    )

    email = StringField(
        'email',
        validators=[DataRequired(), Email()],
    )

    gender = SelectField(
        'gender',
        choices=['Male', 'Female', 'Other'],
        validators=[optional()]
    )

    dob = DateField(
        'Date of Birth',
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,15)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(),Length(5,15),EqualTo('password')]
    )

    submit = SubmitField(
        'Sign Up'
    )


class LoginForm(FlaskForm):
    email = StringField(
        'email',
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5, 15)]
    )
    remember_me = BooleanField(
        'Remember Me',
    )
    submit = SubmitField('Log In')