import re
import jwt
import config

from datetime import datetime
from tekoapp import models, repositories, helpers
from tekoapp.extensions import exceptions


def create_user_to_signup_request(username, email, password, **kwargs):
    if (
        username and helpers.Username(username).is_valid()
        and
        email and helpers.Email(email).is_valid()
        and
        password and helpers.Password(password).is_valid()
    ):
        existed_user = repositories.user.find_one_by_email_or_username_in_user(
            email, username)
        existed_user_not_verify = repositories.signup.find_one_by_email_or_username_in_signup_request(
            email, username)
        if existed_user or existed_user_not_verify:
            raise exceptions.BadRequestException(
                "User with username {username} "
                "or email {email} already existed!".format(
                    username=username,
                    email=email
                )
            )
        user = repositories.signup.save_user_to_signup_request(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
        
        content_mail = "Thankyou for use TEKOAPP. You token: " + user.user_token_confirm
        check_send_mail = repositories.sendmail.send_mail("Information Veriry Account.", content_mail, email)
        if (check_send_mail):
            return user
        else:
            exceptions.ForbiddenException(message="Not found email!!!")
    else:
        raise exceptions.BadRequestException("Data invalid!")


def verify(token_string):
    try:
        token_data = jwt.decode(token_string, config.FLASK_APP_SECRET_KEY)
    except jwt.ExpiredSignature:
        check_del_signup_request = repositories.signup.delete_by_token_in_signup_request(token_string)
        if check_del_signup_request:
            raise exceptions.UnAuthorizedException('expired token, delete account')
        else:
            raise exceptions.BadRequestException('database error')

    username = token_data["username"]
    user = repositories.signup.find_one_by_email_or_username_in_signup_request(email="", username=username)
    if user:
        repositories.signup.delete_one_by_email_or_username_in_signup_request(user)
        now = datetime.timestamp(datetime.now())
        expired = datetime.timestamp(user.expired_time)
        if expired - now >= 0:
            #function add info to user and delete Signup_Request
            result = repositories.signup.save_user_to_user(
                username=user.username,
                email=user.email,
                password=user.password_hash
            )
            if result is None:
                raise exceptions.BadRequestException("database error")
            else:
                return { 'message' : 'success' }
    raise exceptions.NotFoundException(message="not found user")
