import sqlite3
from cryptography.fernet import Fernet
import os

# File is data.db.enc

class Decryption:
    def __init__(self) -> None:
        # load key
        with open("key.key", "rb") as key:
            data = key.read()
        
        # load db
        with open("data.db.enc", "rb") as database_encrypted:
            database = database_encrypted.read()

        self.fernet = Fernet(key=data)

        content = self.fernet.decrypt(database)

        with open("temp.db", "wb") as dbd:
            dbd.write(content)

    def operations(self):
        