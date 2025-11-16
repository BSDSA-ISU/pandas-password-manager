import sqlite3
from cryptography.fernet import Fernet
import os
from utils import firstrun
from utils import Encryption

firstrun.firstrun()

# File is data.db.enc

class Decryption:
    @staticmethod
    def Decrypt():
        # load key

        if os.path.isfile("key.key"):
            with open("key.key", "rb") as key:
                data = key.read()
                fernet = Fernet(key=data)

        # load db
        if os.path.isfile("data.db.aes"):
            with open("data.db.aes", "rb") as database_encrypted:
                database = database_encrypted.read()

            content = fernet.decrypt(database)

            with open("temp.db", "wb") as dbd:
                dbd.write(content)

    def Insert(self, website, username, password):
        Decryption.Decrypt()

        # Open the decrypted database
        conn = sqlite3.connect("temp.db")
        cursor = conn.cursor()
        
        # Commands execute
        cursor.execute("CREATE TABLE IF NOT EXISTS passwords (website TEXT, username TEXT, password TEXT)")
        cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, password))
        conn.commit()
        conn.close()

        # Encrypt back the database
        Encryption.Encrypt()

    def Show(self, Search=""):
        Decryption.Decrypt()
        con = sqlite3.connect("temp.db")
        cursor = con.cursor()

        if Search == "":
            cursor.execute("SELECT * FROM passwords")
        else:
            cursor.execute("SELECT * FROM passwords WHERE website LIKE ?", (f"%{Search}%",))

        for row in cursor.fetchall():
            print("Password for", row[0], "with username", row[1], "is:", row[2])

        Encryption.Encrypt()

    def Delete(self, website, username, password):
        Decryption.Decrypt()

        # Delete an entry in db

        con = sqlite3.connect("temp.db")
        cursor = con.cursor()

        cursor.execute(
            "DELETE FROM passwords WHERE website = ? AND username = ? AND password = ?",
            (website, username, password)
        )

        con.commit()
        con.close()

        Encryption.Encrypt()

    def EntryCount(self):
        Decryption.Decrypt()

        # counts how many lines are on database

        con = sqlite3.connect("temp.db")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM passwords")

        for _ in cursor.fetchall():
            count=+1
        
        print("there is", count, "entries")