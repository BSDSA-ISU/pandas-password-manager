from cryptography.fernet import Fernet
import os

class Check:
    def __init__(self):
        try:
            self.keys = open("key.key", "rb").read()
            self.r = Fernet(key=self.keys)
            del self.keys
        except:
            pass


    def IsKeyMatched(self):
        if os.path.isfile("./password.csv.ali") != True and not os.path.isfile("./key.key"):
            return True
        try:
            data = open("passwords.csv.ali", "rb").read()
            self.r.decrypt(data)
            return True
        except Exception:
            return False

tre = Check()

def Checkit():
    if tre.IsKeyMatched() == False:
        return False
    else:
        return True
