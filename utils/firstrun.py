from cryptography.fernet import Fernet
import os

if not os.path.isfile("key.key"):
    b = Fernet.generate_key()
    with open("key.key", 'xwb') as key:
        key.write(b)
else:
    print("key exists!")