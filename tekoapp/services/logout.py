import jwt
import config
from tekoapp import repositories

from tekoapp.extensions import exceptions

def check_token_from_logout_request(tokenstring):
    token_data = jwt.decode(tokenstring, config.FLASK_APP_SECRET_KEY)
    if token_data:
        checkdel =  repositories.usertoken.delete_token_by_tokenstring(tokenstring)
        if checkdel:
                return { 'message' : 'Log out susscess!' }
        else:
                raise exceptions.BadRequestException("Database error!")
    else:
        raise exceptions.BadRequestException("Token expired!")

