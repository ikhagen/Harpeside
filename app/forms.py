from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ContactForm(Form):
    name = StringField('name')
    email = StringField('email', validators=[DataRequired()])
    phone = IntegerField('phone')
    message = StringField('message')
