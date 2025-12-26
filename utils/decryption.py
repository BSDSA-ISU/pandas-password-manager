import sqlite3
from cryptography.fernet import Fernet
import os
from utils import firstrun
from utils import Encryption
import sys

firstrun.firstrun()

# File is data.db.enc

class Decryption:
    @staticmethod
    def Decrypt():
        # load key

        if os.path.isfile("./PersonalFiles/key.key"):
            with open("./PersonalFiles/key.key", "rb") as key:
                data = key.read()
                fernet = Fernet(key=data)

        # load db
        if os.path.isfile("./PersonalFiles/data.db.aes"):
            with open("./PersonalFiles/data.db.aes", "rb") as database_encrypted:
                database = database_encrypted.read()

            try:
                content = fernet.decrypt(database)
            except Exception:
                print("Invalid key provided or lost key. Is your key vaild or matched?")
                sys.exit(1)

            with open("temp.db", "wb") as dbd:
                dbd.write(content)

    def Update(self, website, username, new_password):
        Decryption.Decrypt()
        con = sqlite3.connect("temp.db")
        cursor = con.cursor()

        # Check if the entry exists
        cursor.execute("SELECT * FROM passwords WHERE website LIKE ? AND username LIKE ?", 
                   (f"%{website}%", f"%{username}%"))
        result = cursor.fetchone()

        if not result:
            print("No matching entry found.")
            Encryption.Encrypt()
            return

        print("Found entry:")
        print(f"Website: {result[0]}")
        print(f"Username: {result[1]}")
        print(f"Password: {result[2]}")
        print("———————————————")

        # Ask user for confirmation
        confirm = input("Do you want to update the password for this entry? (y/n): ").lower()
        if confirm != "y":
            print("Update cancelled.")
            Encryption.Encrypt()
            return

        # Perform the update
        cursor.execute("UPDATE passwords SET password = ? WHERE website LIKE ? AND username LIKE ?", 
                   (new_password, f"%{website}%", f"%{username}%"))
        con.commit()
        print("Password updated successfully!")

        Encryption.Encrypt()


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
            print(f"Account Website: {row[0]}")
            print(f"Username: {row[1]}")
            print(f"Password: {row[2]}")
            print("———————————————")


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
        count = 0
        for _ in cursor.fetchall():
            count = count + 1
        
        print("there is", count, "entries")

    def Show_website(self):
        Decryption.Decrypt()

        con = sqlite3.connect("temp.db")
        cursor = con.cursor()

        cursor.execute("SELECT website FROM passwords ORDER BY website COLLATE NOCASE;")

        x = cursor.fetchall()

        # Print all websites
        for _ in x:
            print(_)

    @staticmethod
    def Check():
        Decryption.Decrypt()
        try:
            os.remove("temp.db")
        except Exception:
            pass
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')



"""

SELECT *
FROM passwords
ORDER BY website COLLATE NOCASE;

"""