from flask_mail import Message
from flask import render_template
from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def contact_email(sender, message):
    send_email("Message from harpeside",
               sender,
               'idakhagen@gmail.com',
               render_template("contact_request.txt",
                               sender=sender, message=message),
               render_template("contact_request.html",
                               sender=sender, message=message))








