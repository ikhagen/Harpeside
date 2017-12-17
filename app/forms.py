from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class ContactForm(Form):
    email = StringField('email', validators=[DataRequired()])
    message = StringField('message')
