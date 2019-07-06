from tekoapp.extensions import exceptions
from tekoapp import repositories

def check_info_and_res(username="", email="", newpassword="", **kwarg):
    print(username)
    print(email)
    print(newpassword)
    user = repositories.user.find_user_by_username_and_email(username, email)
    if user is None:
        raise exceptions.BadRequestException("User not exist!")
    else:
        #function check
        if repositories.changepassword.update_password(newpassword, user):
            return { "message": "Change password success" }
        else:
            return { "message": "Change Error" }