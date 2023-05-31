from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class Get_Pokemon_Form(FlaskForm):
    get_pokemon = StringField('Get Pokemon', validators=[DataRequired()])
    submit_btn = SubmitField('Search')