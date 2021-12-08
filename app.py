from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'WELCOME TO SERVER SIDE!'

@app.route('/about')
def me():
    return 'IM EDEN AND I LOVE WEB, we just started to learn serer side'

@app.route('/redirect')
def redi():
 return redirect('/about')

@app.route('/ur')
def foru():
 return redirect(url_for('me'))

if __name__ == '__main__':
    app.run()