from tekoapp.extensions import exceptions
from tekoapp import repositories, helpers

def check_info_and_res(username="", email="", password="", newpassword="", **kwarg):
    if(
        username and helpers.Username(username).is_valid()
        and
        email and helpers.Email(email).is_valid()
        and
        newpassword and helpers.Password(newpassword).is_valid()
    ):
        user = repositories.user.find_user_by_username_and_email(username, email)
        if user is None:
            raise exceptions.BadRequestException("User not exist!")
        else:
            #function check
            print(password)
            if ( user.check_password(password) ):
                if repositories.changepassword.update_password(newpassword, user):
                    return { "message": "Change password success" }
                else:
                    raise exceptions.UnAuthorizedException(message="new password equal password")
            else:
                raise exceptions.UnAuthorizedException(message="Password invalid")
    else:
        raise exceptions.BadRequestException("Data invalid!")