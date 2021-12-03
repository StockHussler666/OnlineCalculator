from flask import Flask, render_template
from flask.globals import request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'HelloWorld'

class NumberForm(FlaskForm):
    number1 = IntegerField('Enter your first number')
    number2 = IntegerField('Enter your second number')
    submit1 = SubmitField('Multiply')
    submit2 = SubmitField('Add')
    submit3 = SubmitField('Minus')
    submit4 = SubmitField('Divide')

def mulitpy(a,b):
    return a*b

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def divide(a,b):
    return a/b

@app.route('/', methods=['GET','POST'])
def index():
    name = 'Calculator'
    solution = ""
    form=NumberForm()
    number1 = form.number1.data
    number2 = form.number2.data
    if form.validate_on_submit():
        if form.submit1.data:
            solution = str(mulitpy(number1,number2))
            return render_template('index.html', name=name, form=form, solution=solution)
        elif form.submit2.data:
            solution = str(add(number1,number2))
            return render_template('index.html', name=name, form=form, solution=solution)
        elif form.submit3.data:
            solution = str(minus(number1,number2))
            return render_template('index.html', name=name, form=form, solution=solution)
        elif form.submit4.data:
            try:
                solution = str(divide(number1,number2))
                return render_template('index.html', name=name, form=form, solution=solution)
            except ZeroDivisionError:
                return render_template('index.html', name=name, form=form, solution='You cannot divide by zero')
    return render_template('index.html', name=name, form=form, solution=solution)

if __name__== '__main__':
    app.run(debug=True)