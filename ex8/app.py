from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('CVgrid.html')

@app.route('/exe2')
def ex2():  # put application's code here
    return render_template('exercise2.html')

@app.route('/forms')
def form():  # put application's code here
    return render_template('forms.html')

@app.route('/about me')
def me():  # put application's code here
    return render_template('about me.html')

@app.route('/assignment8')
def ex8():  # put application's code here
    name='EDEN MORAN'
    age='24'
    hobbies = ['macrame', 'yoga', 'bake', 'cook', 'gym']
    hobby = 'cook'
    return render_template('assignment8.html', hobbies=hobbies, hobby=hobby, name=name, age=age)


if __name__ == '__main__':
    app.run()
