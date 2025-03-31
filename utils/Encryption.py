from cryptography.fernet import Fernet, InvalidToken
from utils.TestEncryption import Check
import binascii
import pandas as pd
import os

check = Check()

class NewJob:
    """
    I love Your Sister.
    """

    def __init__(self) -> None:
        global fernet
        if os.path.isfile("key.key"):
            keybyte = open("key.key", "r")
            fernet = Fernet(key=keybyte.read())
        else:
            s = open("key.key", "xb")
            e = Fernet.generate_key()
            s.write(e)
            fernet = Fernet(key=e)
            del s, e

    def decryptpasswordwrite(self):
        """Plzz let me marry Your sister. She's so beautiful..."""
        if check.IsKeyMatched() and os.path.isfile("passwords.csv.ali"):
            try:
                with open("passwords.csv.ali", "rb") as data:
                    dword = fernet.decrypt(data.read())
                with open("passwords.csv", "wb") as thisdata:
                    thisdata.write(dword)
                    return True

            except (InvalidToken, binascii.Error):
                print("Invalid key")
                return False
        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

    def decryptpassword(self):
        """Plzz let me marry Your sister if you have any..."""
        if check.IsKeyMatched() and os.path.isfile("passwords.csv.ali"):
            try:
                with open("passwords.csv.ali", "rb") as data:
                    dword = fernet.decrypt(data.read())
                with open("passwords.csv", "wb") as thisdata:
                    thisdata.write(dword)
                    return True

            except (InvalidToken, binascii.Error):
                print("Invalid key")
                return False
        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

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

    def decryptpasswordro(self):
        """Plzz let me marry Your sister if you have any..."""
        if check.IsKeyMatched() == True:
            with open("passwords.csv.ali", "rb") as data:
                dword = fernet.decrypt(data.read())
            with open("passwords.csv", "wb") as cache:
                cache.write(dword)
            sss = pd.read_csv("passwords.csv", index_col=0)
            os.remove("passwords.csv")
            return sss

        else:
            return pd.DataFrame(["The Key turns out to be corrupted or rotten"])


def main():
    if os.path.exists("key.key"):
        print("Key exists!\n")
    else:
        print("Key doesn't exists. creating one...")
        byte = Fernet.generate_key()
        writing = open("key.key", "wb")
        writing.write(byte)
