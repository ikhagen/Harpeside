from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class ContactForm(Form):
    name = StringField('name')
    email = StringField('email', validators=[DataRequired()])
    phone = StringField('phone')
    message = StringField('message')
