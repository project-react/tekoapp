from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/tekoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(300))
    is_active = db.Column(db.Boolean)
    last_login = db.Column(db.DATETIME)
    is_admin = db.Column(db.Boolean)
    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)


class User_token(db.Model):
    __tablename__='user_token'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    token = db.Column(db.Text)
    expired_time = db.Column(db.DateTime)

class Sigup_request(db.Model):
    __tablename__='sigup_request'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(300))
    is_admin = db.Column(db.Boolean)
    expired_time = db.Column(db.DateTime)
    user_token_confirm = db.Column(db.Text)

