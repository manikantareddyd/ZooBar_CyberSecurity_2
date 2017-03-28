from zoodb import *
from debug import *

import hashlib
import random
from os import urandom
import pbkdf2

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    salt = cred.salt
    password = pbkdf2.PBKDF2(password, salt).hexread(32)
    if not cred:
        return None
    if cred.password == password:
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    db = person_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    db.add(newperson)
    db.commit()

    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred:
        return None
    newcred = Cred()
    newcred.username = username
    
    salt = urandom(8).encode('base-64')
    password = pbkdf2.PBKDF2(password, salt).hexread(32)

    newcred.password = password
    newcred.salt = salt
    db.add(newcred)
    db.commit()
    return newtoken(db, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

