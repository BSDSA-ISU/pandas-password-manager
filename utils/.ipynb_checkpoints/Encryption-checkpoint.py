from cryptography.fernet import Fernet, InvalidToken
import binascii
import os

returns = None

class NewJob:
    """
    I love Your Sister.
    """
    def __init__(self) -> None:
        keybyte = open("key.key", "r")
        global fernet
        fernet = Fernet(key=keybyte.read())

    def decryptpassword(self) -> None:
        """Plzz let me marry Your sister if you have any..."""
        try:
            with open("passwords.csv", "rb") as data:
                dword = fernet.decrypt(data.read())
            with open("passwords.csv", "wb") as thisdata:
                thisdata.write(dword)
        except (InvalidToken, binascii.Error):
            print("Oh my got")
            raise 

    def encryptpasswords(self):
        try:
            with open("passwords.csv", "rb") as data:
                dword = fernet.encrypt(data.read())
            with open("passwords.csv", "wb") as thisdata:
                thisdata.write(dword)
        except (binascii.Error):
            print("OHmygot")
            raise

def main():
    if os.path.exists("key.key"):
        print("Key exists!\n")
    else:
        print("Key doesn't exists. creating one...")
        byte = Fernet.generate_key()
        writing = open("key.key", "wb")
        writing.write(byte)

