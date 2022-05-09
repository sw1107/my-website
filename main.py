from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

Bootstrap(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        pass
        # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=my_password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs=my_email,
        #         msg=f"Subject:Website email from {contact_form.name.data}, {contact_form.email.data}"
        #             f"\n\n{contact_form.message.data}"
        #     )
        # flash("Message Sent")
        # return redirect('/#contact')
    else:
        return render_template('index.html', contact_form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)