import os
import requests

from flask import Flask, request, render_template, redirect
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()
Bootstrap(app)
backend_url = os.getenv('BACKEND_URL', 'http://localhost:1323')
HTTP_METHODS = ["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]


class RequestForm(FlaskForm):
    method = SelectField("Method", choices=HTTP_METHODS)
    body = StringField("Body")
    submit = SubmitField('Send')
    response = TextAreaField("Response from Backend")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RequestForm(request.form)

    if request.method == 'POST' and form.validate():
        response = requests.request(form.method.data,
                                    backend_url, data=form.body.data)
        form.response.data = response.content.decode('UTF-8')
        redirect('index')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
