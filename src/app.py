from flask import render_template, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, DecimalField, FloatField
from wtforms.validators import DataRequired, Optional
import math
import os

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
    )


class ExpresionForm(FlaskForm):
    variableName1 = StringField('User defined variable 1', validators=[DataRequired()], render_kw={"placeholder": "name"})
    variableValue1 = FloatField('User defined variable 1', validators=[Optional()], render_kw={"placeholder": "value"})
    variableName2 = StringField('User defined variable 2', validators=[Optional()], render_kw={"placeholder": "name"})
    variableValue2 = FloatField('User defined variable 2', validators=[Optional()], render_kw={"placeholder": "value"})
    code = TextAreaField(u'Code', validators=[DataRequired()])
    submit = SubmitField('Evaluate')


def calculate_forward(spot, rate, div_rate):
    return spot * math.exp(rate - div_rate)


@app.route('/', methods = ['POST', 'GET'])
def login():
    form = ExpresionForm()
    locApp = {'alfa': 5.0, 'beta': 2.2, 'gamma': 3.4}
    if form.validate_on_submit():
        code = form.code.data
        locRes = dict(locApp)
        locRes['calculate_forward'] = calculate_forward
        locRes[form.variableName1.data] = form.variableValue1.data
        if form.variableName2.data:
            locRes[form.variableName2.data] = form.variableValue2.data
        exec(code, {}, locRes)
        return render_template('index.html', title='', form=form, appVariables=locApp, resVariables=locRes)
    return render_template('index.html', title='', form=form, appVariables=locApp, resVariables='')


if __name__ == '__main__':
    app.run()
