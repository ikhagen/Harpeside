from flask_mail import Message
from flask import render_template
from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def contact_email(name, email, phone, message):
    send_email("Nokon har sendt deg ei melding fra harpeside",
               email,
               ['idakhagen@gmail.com'],
               render_template("contact_request.txt",
                               sender=email, name=name, phone=phone, message=message),
               render_template("contact_request.html",
                               sender=email, name=name, phone=phone, message=message))








