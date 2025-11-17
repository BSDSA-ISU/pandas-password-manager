from utils.decryption import Decryption
from utils.Encryption import Encrypt
from colorama import Fore

print(f"{Fore.GREEN} Be {Fore.RESET}")

decrypt = Decryption()

decrypt.Insert("agoogle", "alie", "123456")
decrypt.Show_website()
decrypt.Show()

