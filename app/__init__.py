from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)
app.config.from_object('config')

from app import views
