from cryptography.fernet import Fernet
import os
    
# Encrypts the passowrd file back and deletes the unencrypted one
def encryptpasswords():
    with open("./key.key", "rb") as ke:
        keyu = ke.read()
    fernet = Fernet(key=keyu)

    try:
        with open("passwords.csv", "rb") as data:
            dword = fernet.encrypt(data.read())
        with open("passwords.csv.ali", "wb") as thisdata:
            thisdata.write(dword)
            return True
    except Exception:
        raise SyntaxError("Eee")

# Simple initialator if the password.csv and password.csv.aes is misseng
def make_password_file():
    passfile = open("passwords.csv", "w")
    passfile.write("│user│website│password\n")

def make_key():
    e = Fernet.generate_key()
    with open("key.key", "wb") as key:
        key.write(e)
    return e