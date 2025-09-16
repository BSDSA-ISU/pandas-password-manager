from cryptography.fernet import Fernet

# Simple initialator if the password.csv and password.csv.aes is misseng
def make_password_file():
    passfile = open("passwords.csv", "w")
    passfile.write("│user│website│password\n")

def make_key():
    s = open("key.key", "xb")
    e = Fernet.generate_key()
    s.write(e)
    del s, e