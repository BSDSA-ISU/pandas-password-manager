from cryptography.fernet import Fernet, InvalidToken
from utils.TestEncryption import Checkit as check
import binascii
import pandas as pd
import os
from utils.FirstInit import make_password_file, make_key

class Encrypt:

    def __init__(self) -> None:
        global fernet
        if os.path.isfile("key.key"):
            keybyte = open("key.key", "r")
            fernet = Fernet(key=keybyte.read())
        else:
            keyfile = make_key()
            fernet = Fernet(key=keyfile)

        # File check
        if os.path.isfile("./passwords.csv.ali") == False and os.path.isfile("./passwords.csv") == False:
            make_password_file()

    # Encrypts the passowrd file back and deletes the unencrypted one
    def encryptpasswords(self):
        try:
            with open("passwords.csv", "rb") as data:
                dword = fernet.encrypt(data.read())
            with open("passwords.csv.ali", "wb") as thisdata:
                thisdata.write(dword)
                os.remove("passwords.csv")
                return True
        except Exception:
            raise SyntaxError("Eee")


# this executes if there is no key present
def main():
    if os.path.exists("key.key"):
        print("Key exists!\n")
    else:
        print("Key doesn't exists. creating one...")
        byte = Fernet.generate_key()
        writing = open("key.key", "wb")
        writing.write(byte)
