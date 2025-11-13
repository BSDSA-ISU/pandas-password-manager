from cryptography.fernet import Fernet
import os

def firstrun():
    if not os.path.isfile("key.key"):
        b = Fernet.generate_key()
        with open("key.key", 'wb') as key:
            key.write(b)
    else:
        print("key exists!")