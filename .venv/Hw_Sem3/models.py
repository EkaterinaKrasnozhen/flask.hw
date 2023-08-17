from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    birth = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=True, nullable=False)
    
    
    def __repr__(self):
        return f'User({self.username}, {self.email})'