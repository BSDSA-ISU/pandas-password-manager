from utils.TestEncryption import Checkit as check
from cryptography.fernet import InvalidToken, Fernet
from utils.FirstInit import make_password_file, make_key
import os
import binascii
import pandas as pd

class Decrypt:

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

    def decryptpasswordwrite(self):
        # Checks if the keyfile can be used to decrypt the password file
        if check() and os.path.isfile("passwords.csv.ali"):
            try:
                with open("passwords.csv.ali", "rb") as data:
                    dword = fernet.decrypt(data.read())
                with open("passwords.csv", "wb") as thisdata:
                    thisdata.write(dword)
                    return True

            # throws this if there is corruption(different from mismatched key)
            except (InvalidToken, binascii.Error):
                print("Invalid data")
                return False

        # If the key is incorrect. it throws this
        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

    def decryptpassword(self):

        # Checks if the keyfile can be used to decrypt the password file
        if os.path.isfile("passwords.csv.ali"):
            try:
                with open("passwords.csv.ali", "rb") as data:
                    dword = fernet.decrypt(data.read())
                with open("passwords.csv", "wb") as thisdata:
                    thisdata.write(dword)
                    return True

            # throws this if there is corruption(different from mismatched key)
            except (InvalidToken, binascii.Error):
                print("Invalid key")
                return False

        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

    # decrypts the password on read only(shows the password and exits)
    def decryptpasswordro(self):

        if check() == True:
            with open("passwords.csv.ali", "rb") as data:
                dword = fernet.decrypt(data.read())
            with open("passwords.csv", "wb") as cache:
                cache.write(dword)
            sss = pd.read_csv("passwords.csv", index_col=0)
            os.remove("passwords.csv")
            return sss

        else:
            return pd.DataFrame(["The Key turns out to be corrupted, mismatched or rotten"])

