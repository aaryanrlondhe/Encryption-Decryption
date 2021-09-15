from Encryption import encrypt
from Decryption import decrypt

choice=int(input("Enter Your Option\n 1. Encryption\n 2. Decryption\n"))
if choice==1:
    encrypt()
elif choice==2:
    decrypt()
else:
    print("Please Enter Correct Option")