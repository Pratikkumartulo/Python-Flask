from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField
from wtforms.validators import DataRequired, Length,Email,optional

class SignupForm(FlaskForm):
    username = StringField(
        'username',
        validators=[DataRequired(), Length(4,25)],
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