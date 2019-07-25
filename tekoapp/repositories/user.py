from sqlalchemy import or_, and_

from tekoapp import models


def save_user_to_user(**kwargs):
    # user = models.Signup_Request(**kwargs)
    # models.db.session.add(user)
    # models.db.session.commit()
    return None

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
    user_in_signup_request = models.Signup_Request.query.filter(
        models.Signup_Request.username == username
        or
        models.Signup_Request.email == email
    ).first()
    return None

def delete_one_by_email_or_username_in_user(user):
    models.db.session.delete(user)
    models.db.session.commit()


def get_list_user():
    return models.User.query.all()