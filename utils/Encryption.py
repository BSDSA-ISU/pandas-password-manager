from cryptography.fernet import Fernet, InvalidToken
from utils.TestEncryption import Checkit as check
import binascii
import pandas as pd
import os

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
        # File check
        if os.path.isfile("./password.csv.ali") == False or os.path.isfile("./password.csv") == False:
            make_password_file()

    def decryptpasswordwrite(self):
        """Plzz let me marry Your sister. She's so beautiful..."""

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
        """Plzz let me marry Your sister if you have any..."""

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
                print("Invalid key")
                return False

        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

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

    # decrypts the password on read only(shows the password and exits)
    def decryptpasswordro(self):
        """Plzz let me marry Your sister if you have any..."""

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

# this executes if there is no key present
def main():
    if os.path.exists("key.key"):
        print("Key exists!\n")
    else:
        print("Key doesn't exists. creating one...")
        byte = Fernet.generate_key()
        writing = open("key.key", "wb")
        writing.write(byte)

# create the .csv password file if it doesn't exist
def make_password_file():
    passfile = open("myass", "w")
    passfile.write("│user│website│password\n")
    passfile.write("0│example│example│example")





