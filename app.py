from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
    )


string='''def power(x) 
return x*x
'''

class ExpresionForm(FlaskForm):
    expression = StringField('Expression', validators=[DataRequired()])
    submit = SubmitField('Evaluate')

@app.route('/')
def hello_world():
    y = 5
    z = 0
    #loc = {'y': y, 'z': z}
    exec(open(os.path.join(os.getcwd(),"script.txt")).read(), {}, {'y': y, 'z': z})
    return 'Hello World! ' + str(z)

@app.route('/index')
def index():
    form = ExpresionForm()
    return render_template('index.html', title='Sign In', form=form)


if __name__ == '__main__':
    print('aaaa')
    app.run()
