import utils.Password as passwd
#from utils import Encryption


println = print
def loop():
    terminator = True
    x = passwd.Password()
    while terminator:
        user = input("User or email \n >>")
        web = input("Websites you log on \n >>")
        password = input("Password\n>>")
        x.Insert(user, web, password)
        println("Do you want to insert another entry?")
        y = input("(Y/N)>>")
        if y.lower() == "y":
            terminator = True
        else:
            terminator = False
        
loop()
