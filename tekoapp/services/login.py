import re
import jwt

from tekoapp import models, repositories
from tekoapp.extensions import exceptions

def check_info_from_login_request(username, password, **kwargs):
    if(
        len(username) > 5 
    ):
        user = repositories.user.find_user_by_username(username)
        if user is None:
            raise exceptions.BadRequestException("Not found user")
        else:
            if(user.check_password(password)):
                # function add tocken 
                token = repositories.usertoken.create_token_by_user(user)
                if token is None:
                    raise exceptions.BadRequestException("Don't insert token") 
                else:
                    return models.User.check_password(user,password)
            else:
                raise exceptions.BadRequestException("Password invalid") 
    else:
        raise exceptions.BadRequestException("Invalid user data specified!")