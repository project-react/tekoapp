from sqlalchemy import or_, and_
from datetime import datetime
from tekoapp import models

from . import resetpassword

def find_user_by_username(username=""):
    user = models.User.query.filter(
        models.User.username == username
    ).first()
    return user or None

def find_user_by_id(user_id):
    user = models.User.query.filter(
        models.User.id == user_id
    ).first()
    return user or None

def find_user_by_username_and_email(username="", email=""):
    user = models.User.query.filter(
        and_(
            models.User.username == username, 
            models.User.email == email
        )
    ).first()
    return user or None

def find_one_by_email_or_username_in_user(email="", username=""):
    user = models.User.query.filter(
        or_(
            models.User.username == username,
            models.User.email == email
        )
    ).first()
    return user or None

def delete_one_by_email_or_username_in_user(user):
    models.db.session.delete(user)
    models.db.session.commit()

def edit_username_email_is_admin_in_user(new_username, new_email, new_is_admin, user):
    user.username = new_username
    user.email = new_email
    user.is_admin = new_is_admin
    user.updated_at = datetime.now()
    models.db.session.add(user)
    models.db.session.commit()
    return user

def check_orther_user_had_username_email(userid, new_username, new_email):
    list_orther_user = models.User.query\
        .filter(models.User.id != userid).all()
    for user in list_orther_user:
        if (user.username == new_username or user.email == new_email):
            return False
    return True

def add_user_by_username_and_email(username, email, is_admin):
    password = resetpassword.random_password()
    user = {
        'username': username,
        'email': email,
        'password': password,
        'is_admin': is_admin,
        'is_active': True
    }
    new_user = models.User(**user)
    models.db.session.add(new_user)
    models.db.session.commit()
    if new_user:
        return {
            'info': new_user,
            'password': password
        }
    return None

def add(data):
    User = models.User(**data)
    models.db.session.add(User)
    models.db.session.commit()
    return User or None

def edit_look_time_in_user(user, look_time):
    user.look_time = look_time
    user.look_create_at = datetime.now()
    models.db.session.add(user)
    models.db.session.commit()
    return  user or None

def edit_is_active_in_user(user, is_active):
    user.is_active = is_active
    models.db.session.add(user)
    models.db.session.commit()
    return user or None

def get_list_user():
    return models.User.query.all()