from tekoapp import models


def create_token_by_user(user):
    data = {
        'user_id' : user.id, 
    }
    token = models.User_Token(**data)
    models.db.session.add(token)
    models.db.session.commit()
    return token or None

def find_usertoken_by_tokenstring(tokenstring):
    return models.User_Token.query.filter(
        models.User_Token.token == tokenstring
    ).first()

def delete_token_by_tokenstring(tokenstring):
    #find usertoken by tokenstring
    user_token = find_usertoken_by_tokenstring(tokenstring)
    models.db.session.delete(user_token)
    models.db.session.commit()