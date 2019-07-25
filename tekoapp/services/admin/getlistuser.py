from tekoapp import repositories, helpers

@helpers.check_token_and_verify_admin
def get_list_user(token):
    listuser = repositories.user.get_list_user()
    if listuser:
        print(listuser)
        responseListUser = []
        for user in listuser:
            e = {
                'username': user.username,
                'email': user.email,
            }
            responseListUser.append(e)
        return responseListUser
    else:
        raise exceptions.UnAuthorizedException('Server error')