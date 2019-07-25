import enum
import logging
from flask_restplus import fields
from datetime import datetime, timedelta


from tekoapp.models import db, bcrypt


class History_Pass_Change(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    __tablename__ = 'history_pass_changes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    pass_change_history = db.Column(db.Text(), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.pass_change_history = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.pass_change_history, password)

