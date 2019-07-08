import re
import jwt

from tekoapp import models, repositories, helpers
from tekoapp.extensions import exceptions
from datetime import datetime

def check_info_from_login_request(username, password, **kwargs):
    if(
        username and helpers.Username(username).is_valid()
        and
        password and helpers.Password(password).is_valid()
    ):
        user = repositories.user.find_user_by_username(username)
        if user is None:
            raise exceptions.UnAuthorizedException(message="Not found user")
        else:
            if(user.check_password(password)):
                # function add tocken 
                user_token = repositories.usertoken.create_token_by_user(user)
                if user_token is None:
                    raise exceptions.UnAuthorizedException(message="Don't insert token")
                else:
                    int_time = datetime.timestamp(user_token.expired_time)
                    return {
                        'token' : user_token.token,
                        'expired_time' : int_time, 
                    }
            else:
                raise exceptions.BadRequestException("Password invalid") 
    else:
        raise exceptions.BadRequestException("Invalid data!")