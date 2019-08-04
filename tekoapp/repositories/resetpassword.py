import random 
from tekoapp import models, repositories, helpers

# def random_password():
#     numuppercase = random.randint(1, 5)
#     numlowercase  = random.randint(1, 7 - numuppercase)
#     num = 8 - numuppercase - numlowercase
#     password = ''
#
#     for n in range(numuppercase):
#         x = random.randint(65, 90)
#         password += chr(x)
#
#     for n in range(numlowercase):
#         x = random.randint(97, 122)
#         password += chr(x)
#
#     for n in range(num):
#         x = random.randint(48, 57)
#         password += chr(x)
#
#     return password

def change_password(user):
    if user is None:
        return None
    else:
        newpassword = ''
        is_loop = True
        while(is_loop):
            newpassword = helpers.random_password()
            is_loop = False == repositories.checkhistorypass.check_history_pass_when_change(user.id, newpassword)
        repositories.checkhistorypass.save_history_pass(userid=user.id, password=newpassword, is_real_pass=False)
        repositories.checkhistorypass.delete_old_password(userid=user.id)
        user.password = newpassword;
        models.db.session.add(user)
        models.db.session.commit()
        return newpassword