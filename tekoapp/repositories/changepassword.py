from tekoapp import models

def update_password(newpassword, user):
    if user.check_password(newpassword):
        return False
    else:
        user.password = newpassword
        models.db.session.add(user)
        models.db.session.commit()
        return True
    
