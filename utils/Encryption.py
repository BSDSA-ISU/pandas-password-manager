from cryptography.fernet import Fernet
import os
import utils.firstrun

def Encrypt():
    if os.path.isfile("key.key"):
        with open("key.key", "rb") as key:
            mykey = key.read()
    else:
        utils.firstrun

    fernet = Fernet(mykey)

    with open("temp.db", "rb") as database_decrypted:
        content = database_decrypted.read()

    with open("data.db.aes", "wb") as database_encrypted:
        database_encrypted.write(fernet.encrypt(content))

    try:
        os.remove("temp.db")
    except:
        pass