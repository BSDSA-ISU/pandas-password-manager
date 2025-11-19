from cryptography.fernet import Fernet
import os
import utils.firstrun

def Encrypt():
    if os.path.isfile("./PersonalFiles/key.key"):
        with open("./PersonalFiles/key.key", "rb") as key:
            mykey = key.read()
            fernet = Fernet(mykey)
            with open("temp.db", "rb") as database_decrypted:
                content = database_decrypted.read()

            with open("./PersonalFiles/data.db.aes", "wb") as database_encrypted:
                database_encrypted.write(fernet.encrypt(content))

        try:
            os.remove("temp.db")
        except:
            pass
        else:
            utils.firstrun.firstrun()