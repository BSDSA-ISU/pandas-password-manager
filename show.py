from utils.Password import Password
from utils.Decryption import Decrypt

passwd = Password()

decrypt = Decrypt()

print(passwd.ShowPasswords())

decrypt.decryptpasswordshowwebsite()

print()

web = input("website\n>>")

x = decrypt.FindWebsite(web)

print(x)