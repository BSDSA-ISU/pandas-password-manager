from utils.TestEncryption import Checkit as check
from cryptography.fernet import InvalidToken, Fernet
from utils.FirstInit import make_password_file, make_key
import os
import binascii
import pandas as pd
import sys
import io

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
                Error("decryption")

        # If the key is incorrect. it throws this
        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

    # Decrypts the passwords
    def decryptpassword(self) -> io.BytesIO:
        """
        decrypts the password file
        """
        # Checks if the keyfile can be used to decrypt the password file
        if os.path.isfile("passwords.csv.ali"):
            try:        
                with open("passwords.csv.ali", "rb") as data:
                    dword = fernet.decrypt(data.read())

                return io.BytesIO(dword)

            # throws this if there is corruption(different from mismatched key)
            except (InvalidToken, binascii.Error):
                Error("decryption")
                return io.BytesIO(b"None")

        else:
            raise SyntaxError("The key doesn't match exiting to prevent damage or destruction on your password")

    # decrypts the password on read only(shows the password and exits)
    def decryptpasswordro(self):

        if check() == True:

            with open("passwords.csv.ali", "rb") as data:
                dword = io.BytesIO(fernet.decrypt(data.read()))

                # Gets the binary value from the memory and decodes it to string
                Decrypted = dword.getvalue().decode("utf-8")

            return pd.read_csv(io.StringIO(Decrypted), index_col=0)

        else:
            return pd.DataFrame(["The Key turns out to be corrupted, mismatched or rotten"])

    # show password and where or what website
    def decryptpasswordshowwebsite(self):
        if check() == True:
            with open("passwords.csv.ali", "rb") as data:
                # Decrypts the content, store it on memory as string!
                dword = io.BytesIO(fernet.decrypt(data.read())).getvalue().decode("utf-8")

            sss = pd.read_csv(io.StringIO(dword), index_col=0)
            alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
            alphaarr = alphabet.split(",")
            a = sss['website'].sort_values(ascending=True).unique() # type: ignore
            for _ in alphaarr:
                print(_.upper(), ": ")

                for __ in a:
                    if __.lower().startswith(_):
                        print("    ", __)
                print()

            del _, __, alphabet, alphaarr
            os.remove("passwords.csv")

            return a

        else:
            return pd.DataFrame(["The Key turns out to be corrupted, mismatched or rotten"])

    def FindWebsite(self, website : str):
        if check() == True:
            with open("passwords.csv.ali", "rb") as data:
                dword = fernet.decrypt(data.read())
        
            with open("passwords.csv", "wb") as cache:
                cache.write(dword)
        
            sss = pd.read_csv("passwords.csv", index_col=0)
            os.remove("passwords.csv")

        entry = sss[sss['website'].str.contains(website, case=False)]
        return entry



def Error(ErrType : str):
    if ErrType.lower() == "decryption":
        print("Invalid key or corrupted key. please provide the correct key.key.")
        exit(9)

    print("Something went wrong")
    sys.exit(1)
