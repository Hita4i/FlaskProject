import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ROOT_DIR}/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    equipment = db.relationship('Equip', backref='users', lazy=True)

    def __repr__(self):
        return f'{self.id} {self.username} {self.email} {self.password}'

class Equip(db.Model):
    __tablename__ = 'equip'
    id = db.Column(db.Integer, primary_key=True)
    equipment = db.Column(db.String(40), nullable=False)
    equipment_number = db.Column(db.Integer(), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.id} {self.equipment} {self.equipment_number} {self.user_id}'

