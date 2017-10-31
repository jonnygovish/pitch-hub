from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
  content = TextAreaField('New Pitch')
  submit = SubmitField('Submit')