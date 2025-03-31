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
            del data
            return True
        except Exception:
            del data
            return False



tre = Check()


