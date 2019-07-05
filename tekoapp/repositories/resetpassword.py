import random 
from tekoapp import models

def random_password():
    numuppercase = random.randint(1, 5)
    numlowercase  = random.randint(1, 7 - numuppercase)
    num = 8 - numuppercase - numlowercase
    password = ''

    for n in range(numuppercase):
        x = random.randint(65, 90)
        password += chr(x)
    
    for n in range(numlowercase):
        x = random.randint(97, 122)
        password += chr(x)

    for n in range(num):
        x = random.randint(48, 57)
        password += chr(x)
   
    return password

def change_password(user):
    if user is None:
        return None
    else:
        newpassword = random_password()
        user.password = newpassword; 
        models.db.session.add(user)
        models.db.session.commit()
        return newpassword