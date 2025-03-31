import pandas as pd
from utils.Encryption import NewJob
import os
from utils.TestEncryption import Check

class Password:
    global newjob, check
    newjob = NewJob()
    check = Check()


    def Insert(self, user, website, password):
        """Let me mary your Sister hehehe!"""
        try:
            newjob.decryptpassword()
            print()
        except Exception:
            pass

        Passwords = pd.read_csv("passwords.csv", index_col=0)

        newentry = pd.DataFrame({"user": [user], "website": [website], "password": [password]})
        Passwords = pd.concat([Passwords, newentry], ignore_index=True)

        Passwords.to_csv("passwords.csv")
        newjob.encryptpasswords()


    def ShowPasswords(self):
        try:
            L = pd.DataFrame(newjob.decryptpasswordro())
            return L
        except Exception:
            raise ValueError("The decryption failed. Invalid or rotten key")
            #pd.read_csv("passwords.csv", index_col=0)
            #raise
        #raise ValueError



