from flask_restplus import fields
from datetime import datetime, timedelta

from tekoapp.models import db, bcrypt

class User_Token(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    __tablename__ = 'user_token'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    token = db.Column(db.Text(), nullable=False)
    expired_time = db.Column(db.TIMESTAMP, default=(datetime.now() + timedelta(minutes=30)))
    update_at = db.Column(db.TIMESTAMP, default=datetime.now())

