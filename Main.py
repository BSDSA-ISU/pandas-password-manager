from colorama import Fore
from utils.Password import Password
from utils.Decryption import Decrypt
from utils.TestEncryption import Checkit

if Checkit():
    pass
else:
    print("key is invalid..")
    exit(9)

decrypt = Decrypt()
passwd = Password()

print("welcome to password manager")
print()
print("Choose what to do:\n")

print(f"{Fore.YELLOW}1. insert a password")
print(f"{Fore.MAGENTA}2. Show password all of it.")
print(f"{Fore.GREEN}3. Show password by website{Fore.RESET}")

try:
    x = int(input("\n>>"))
    if x == 1:
        user = input("User or email \n >>")
        web = input("Websites you log on \n >>")
        password = input("Password\n>>")
        passwd.Insert(user=user, website=web, password=password)
    
    if x == 2:
        print(decrypt.decryptpasswordro())

    if x == 3:
        print()
        decrypt.decryptpasswordshowwebsite()
        website = input("pick a website\n>>")
        print("\nshowing if the website exist..\n")
        print(decrypt.FindWebsite(website))

except Exception:
    print(F"{Fore.RED}User Didn't follow the instruction. exiting{Fore.RESET}")