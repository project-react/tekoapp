from tekoapp import models

def update_password(newpassword, user):
    newpassword_hash =  models.bcrypt.generate_password_hash(
        newpassword).decode('utf-8')
    if newpassword_hash == user.password_hash:
        return False
    else:
        user.password = newpassword
        models.db.session.add(user)
        models.db.session.commit()
        return True
    
