# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

import logging
from flask import Flask, Response, redirect, render_template, request, url_for, make_response, session


app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
        # session['username'] = request.form.get('username') or 'NoName'
        # session['mail'] = request.form.get('mail')
        # response.set_cookie('username', request.form.get('username'))
        # response.set_cookie('e-mail', request.form.get('mail'))
        
    name = request.form['name']
    mail = request.form['email']
    response = make_response(redirect('/greet'))
    response.set_cookie('user_name', name)
    response.set_cookie('e-mail', mail)
    return response


@app.route('/greet/')
def greet():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('greet.html', user_name=user_name)
    return redirect('/')


@app.route('/logout/')
def logout():
    responce = make_response(redirect('/'))
    responce.delete_cookie('user_name')
    responce.delete_cookie('e-mail')
    return responce


if __name__ == '__main__':
    app.run(debug=True)