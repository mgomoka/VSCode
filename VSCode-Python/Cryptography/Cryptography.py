from typing import MutableSet
from cryptography.fernet import Fernet

def generateMasterKey():
    master_key = Fernet.generate_key()
    with open('/Users/matthewgomoka/Documents/VSCode/VSCode-Python/Cryptography/MasterKey.txt', 'w') as master_key_file:
        master_key_file.write(master_key)
