import pandas as pd
from utils.Encryption import NewJob
import os

class Password:
    global newjob
    newjob = NewJob()

    try:
        newjob.decryptpassword()
        print()
    except Exception:
        pass

    def __init__(self) -> None:
        self.Passwords = pd.read_csv("passwords.csv", index_col=0)

    def Insert(self, user, website, password):
        """Let me mary your Sister hehehe!"""

        newentry = pd.DataFrame({"user": [user], "website": [website], "password": [password]})
        self.Passwords = pd.concat([self.Passwords, newentry], ignore_index=True)

        os.remove("passwords.csv")

        self.Passwords.to_csv("passwords.csv")
        newjob.encryptpasswords()

    def ShowPasswords(self):
        print(self.Passwords)
        #raise ValueError



