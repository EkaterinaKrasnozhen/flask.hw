from flask import Flask, render_template, request
from models import db, User
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')
    

@app.cli.command('fill')
def create_base():
    for i in range(1, 11):
        user = User(
            name = 'Kate', lastname = f'Kras_{i}', birth = f'1985-{i}-25', 
            email = f'{i}_mail.mail.ru', password = f'{i}qweasd')
        db.session.add(user)
    db.session.commit()
    
    
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        hash = generate_password_hash(form.password.data)
        user = User(name=form.name.data, lastname=form.lastname.data, birth=form.birth.data, email=form.email.data, password=hash)
        exist_user = User.query.filter((User.lastname == form.lastname.data) | (User.email == form.email.data)).first()
        if exist_user:
            error_msg = 'User allready exist.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)
        db.session.add(user)
        db.session.commit()
        return 'Success!'
    return render_template('register.html', form=form)
    
    
if __name__ == "__main__":
    app.run(debug=True)