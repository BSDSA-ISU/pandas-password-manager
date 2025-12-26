from utils.decryption import Decryption
from colorama import Fore

Decryption.Check()

print("#################################################################################\n")

decryption = Decryption()

print(f"{Fore.GREEN}Welcome to Alieelinux's Password Manager {Fore.RESET}")

print()

print("Choose what to do(automatically creates on First run):")
print("1. Find website and show the passwords")
print("2. Insert a password")
print("3. Delete")
print("4. Show all Entries")
print("5. Update entry")
print("6. exit")

print("\n#############################################################")

x = int(input("\n>>"))

if x == 1:
    Website = input("search for the website\n>>")
    decryption.clear()
    decryption.Show(Search=Website)
if x == 2:
    print("\nThis section adds a password entry\n")
    Website = input("website/platform you logged on\n>>")
    Username = input("Username/gmail/or whatever\n>>")
    Password = input("Pin passords etc\n>>")
    decryption.clear()
    decryption.Insert(website=Website, username=Username, password=Password)
if x == 3:
    print("\nThis section removes a password entry.\n")
    Website = input("website/platform you logged on\n>>")
    Username = input("Username/gmail/or whatever\n>>")
    Password = input("Pin passords etc\n>>")
    decryption.clear()
    decryption.Insert(website=Website, username=Username, password=Password)
if x == 4:
    decryption.clear()
    decryption.Show()
if x == 5:
    website = input("existing website\n>>")
    username = input("esisting Username\n>>")
    password = input("new password\n>>")
    decryption.Update(website=website, username=username, new_password=password)
