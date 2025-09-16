from cryptography.fernet import Fernet

class Check:
    def __init__(self):
        try:
            self.keys = open("key.key", "rb").read()
            self.r = Fernet(key=self.keys)
            del self.keys
        except:
            pass


    def IsKeyMatched(self):
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
