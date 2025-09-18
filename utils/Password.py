import pandas as pd
from utils.Encryption import Encrypt
from utils.Decryption import Decrypt
import os
from utils.TestEncryption import Check
from utils.FirstInit import make_password_file

class Password:
    global newjob, check, encrypt, decrypt
    encrypt = Encrypt()
    decrypt = Decrypt()
    check = Check()

    if os.path.isfile("./passwords.csv") == False and os.path.isfile("./passwords.csv.ali") == False:
        make_password_file()

    def Insert(self, user, website, password):
        """Let me mary your Sister hehehe!"""

        try:
            # File checker if it is the first time you run it
            if os.path.isfile("./passwords.csv.ali"):
                decrypt.decryptpassword()
            else:
                print("This must be the first time you execute this file. continuing...")
        except Exception:
            print("invalid key or first time run")

        if os.path.isfile("./passwords.csv") != False:
            Passwords = pd.read_csv("passwords.csv", index_col=0)
        else:
            print("missing file due to failed decryption. exiting")
            exit(9)
        newentry = pd.DataFrame({"user": [user], "website": [website], "password": [password]})
        Passwords = pd.concat([Passwords, newentry], ignore_index=True)

        Passwords.to_csv("passwords.csv")
        encrypt.encryptpasswords()


    def ShowPasswords(self):
        try:
            L = pd.DataFrame(decrypt.decryptpasswordro())
            return L
        except Exception:
            raise ValueError("The decryption failed. Invalid or rotten key")
            #pd.read_csv("passwords.csv", index_col=0)
            #raise
        #raise ValueError



