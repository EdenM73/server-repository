from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')


@app.route('/')
def home():  # put application's code here
    return render_template('pages/CVgrid/CVgrid.html')


@app.route('/exe2')
def ex2():  # put application's code here
    return render_template('pages/exercise2/exercise2.html')


@app.route('/forms')
def form():  # put application's code here
    return render_template('pages/forms/forms.html')


@app.route('/about me')
def me():  # put application's code here
    return render_template('pages/about/about me.html')


@app.route('/assignment8')
def ex8():  # put application's code here
    name = 'EDEN MORAN'
    age = '24'
    hobbies = ['macrame', 'yoga', 'bake', 'cook', 'gym']
    hobby = 'cook'
    return render_template('pages/assignment8/assignment8.html', hobbies=hobbies, hobby=hobby, name=name, age=age)


@app.route('/assignment9', methods=['GET', 'POST'])
def ex9():
    webUsers = {"user1": {'user name': "Eden111", "user Email": "moranfa15@gmail.com"},
                "user2": {'user name': "Guy123", "user Email": "guy98@gmail.com"},
                "user3": {'user name': "Dina555", "user Email": "dina@gmail.com"},
                "user4": {'user name': "Mordi102", "user Email": "mordi102@gmail.com"},
                "user5": {'user name': "chen7", "user Email": "chen@gmail.com"}}
    thismethod=request.method
    if thismethod == 'GET':
        if 'username' in request.args:
            username = request.args['username']
            if username == '':
                return render_template('pages/assignment9/assignment9.html', Users=webUsers)
            userInput =''
            for user in webUsers.values():
                if user['user name'] == username:
                    userInput = user
            if len(userInput) != 0:
                return render_template('pages/assignment9/assignment9.html', UsersMatch=userInput)
        else:
            return render_template('pages/assignment9/assignment9.html')

    elif thismethod == 'POST':
        username = request.form['username']
        session['username'] = username
        session['login'] = True
        return render_template('pages/assignment9/assignment9.html', username=username)

#assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('pages/assignment9/assignment9.html')


if __name__ == '__main__':
    app.run()
