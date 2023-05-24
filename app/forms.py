from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_btn = SubmitField('Login')

class Get_Pokemon_Form(FlaskForm):
    get_pokemon = StringField('Get Pokemon', validators=[DataRequired()])
    submit_btn = SubmitField('Search')