# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
from flask import escape, flash, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # if 'username' in session:
    #     print(session)
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
    # # return redirect(url_for('login'))
    username = request.cookies.get('session')
    print(username)
    resp = make_response(render_template('forCookie.html'))
    resp.set_cookie('username', 'the username')
    resp.headers['X-Parachutes'] = 'parachutes are cool'
    # return render_template('index.html')
    return resp


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # session['username'] = request.form['username']
        # flash('You were successfully logged in')
        # return redirect(url_for('index'))
        return 'ok'
    # return render_template('login.html', error=error)
    return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
           '''
    # if request.method == 'POST':
    #     if request.form['username'] or request.form['password']:
    #         return request.form['username']
    #     else:
    #         error = 'Invalid username/password'

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('upload_file.txt')
        result = jsonify(code=200, success=True)
        return result


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# set the secret key.  keep this really secret:
# app.secret_key = '123456'

if __name__ == '__main__':
    app.run(debug=True)
