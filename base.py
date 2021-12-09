import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jn5wpthp9gdsfn432lnnvsd'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ROOT_DIR}/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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

def create_db():
    db.create_all()
    db.session.commit()
# n = Equip(equipment='DA', equipment_number=11)
# db.session.add(n)
# db.session.commit()
create_db()