import jwt
import config
from tekoapp import repositories

from tekoapp.extensions import exceptions

def check_info_form_resetpassword_and_res(username, email, **kwargs):
    if(
        # add validation check username and email
        True
    ):
        user = repositories.user.find_user_by_username_and_email(username, email)
        if user is None:
            raise exceptions.BadRequestException("user not exist!")
        else:
            #update value user in database
            newpassword = repositories.resetpassword.change_password(user)
            return newpassword
    else:
        raise exceptions.BadRequestException("form invalid")