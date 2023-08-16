# вариант с сессиями
import logging
from flask import Flask, redirect, render_template, request, url_for, make_response, session


app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'Noname'
        session['mail'] = request.form.get('email')
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)