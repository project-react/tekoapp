import datetime
import enum
import logging

from flask_restplus import fields
from tekoapp.models import db, bcrypt

_logger = logging.getLogger(__name__)


class User(db.Model):
    __tablename__ = 'users'
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(300))
    is_active = db.Column(db.Boolean)
    last_login = db.Column(db.DATETIME)
    is_admin = db.Column(db.Boolean)
    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)


    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
