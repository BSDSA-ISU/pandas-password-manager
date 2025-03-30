import utils.Password as passwd
#from utils import Encryption

x = passwd.Password()

user = input("User or email \n >>")
web = input("Websites you log on \n >>")
password = input("Password\n>>")


x.Insert(user, web, password)

x.ShowPasswords()
