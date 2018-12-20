from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
    )


class ExpresionForm(FlaskForm):
    expression = StringField('Expression', validators=[DataRequired()])
    submit = SubmitField('Evaluate')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    form = ExpresionForm()
    return render_template('index.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
