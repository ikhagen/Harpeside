from flask import render_template, flash, redirect, url_for
from app import app
from .emails import contact_email
from .forms import ContactForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        contact_email(form.name.data, form.email.data, form.phone.data, form.message.data)
        flash('Meldinga er sendt')
        return redirect(url_for('index', _anchor='contact-div'))

    return render_template('home.html',
                           form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html',
                           text='Heider')


@app.route('/contact', methods=['GET', 'POST'])
@app.route('/kontakt', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():

        contact_email(form.email.data, form.message.data)
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.email.data, str(form.message.data)))
        return redirect('/contact')
    return render_template('contact.html',
                           form=form)