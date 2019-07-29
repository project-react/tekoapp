from tekoapp import  repositories, helpers
from tekoapp.extensions import exceptions


@helpers.validator_before_handling
def edit_user(old_username, new_username, new_email, is_admin, **kwargs):
   user = repositories.user.find_user_by_username(old_username)
   if user:
       if (
            user.username != new_username
            or
            user.email != new_email
            or
            user.is_admin != is_admin
       ):
           if repositories.user.edit_username_email_is_admin_in_user(new_username, new_email, is_admin, user):
               return {
                   'message': 'edit success'
               }
           else:
               raise exceptions.BadRequestException('server error')
       else:
           raise exceptions.BadRequestException('User Unchanged')
   else:
       raise exceptions.BadRequestException('Not found user')