from flask import render_template, flash, redirect
from app import app
from .forms import ContactForm

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
@app.route('/kontakt', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.email.data, str(form.message.data)))
        return redirect('/contact')
    return render_template('contact.html',
                           form=form)
