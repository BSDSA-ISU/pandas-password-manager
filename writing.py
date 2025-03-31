from utils.Encryption import NewJob
import os

fff = NewJob()

fff.decryptpasswordwrite()

os.system("vim passwords.csv")
fff.encryptpasswords()
