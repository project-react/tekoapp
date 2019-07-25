from tekoapp import models, repositories as r

def update_password(newpassword, user):
    if user.check_password(newpassword):
        return False
    else:
        if r.checkhistorypass.check_history_pass_when_change(user.id, newpassword):
            r.checkhistorypass.save_history_pass(user.id, newpassword)
            r.checkhistorypass.delete_old_password(user.id)
            user.password = newpassword
            models.db.session.add(user)
            models.db.session.commit()
            return True
        else:
            return  False