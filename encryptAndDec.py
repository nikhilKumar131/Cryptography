from cryptography.fernet import Fernet

# generating the key


def generate_key():
    key = Fernet.generate_key()
    print(key, "is the key")

    # writing key as output file
    with open('keyfile.key', 'wb') as keyfile:
        keyfile.write(key)


def read_key(keyy):
    # read key from file(usable when using specific key)
    with open(keyy, 'rb') as keyfile:
        data.key = keyfile.read()


def encrypt(filee, keyy):
    # read file to encrypt and encrypt
    with open(filee, 'rb') as data:
        orignal = data.read()
        print("Data has been encrypted successfully")

    with open(keyy, 'rb') as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(orignal)

    # writing encrypted data in a file
    with open('encrypted.txt', 'wb') as enc:
        enc.write(encrypted)
        print("encrypted data has been saved as encrypted.txt")


def decrypt(filee,keyy):

    with open(keyy, 'rb') as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    # to decrypt the encrypted data
    with open(filee,'rb') as enc:
        encrypted = enc.read()

    text = fernet.decrypt(encrypted)

    with open(filee,'wb') as dec:
        dec.write(text)
        
    print("your file has been decrypted")


def main():
    print("1. generate_key")
    print("2. encrypt data")
    print("3. decrypt data")
    print("choose the function of your choice: ")
    option = input()
    if option == "1":
        generate_key()
        print("random key is generated")
    elif option == "2":
        print("enter data file name")
        filee = input()
        print("enter key file name.")
        keyy = input()
        encrypt(filee, keyy)
        print("file is encrypted")
    elif option == "3":
        print("enter encrypted file name")
        filee = input()
        print("enter key file name.")
        keyy = input()
        decrypt(filee, keyy)
        print("file is encrypted")
        print("file has been decrypted")
    else:
        print("choose an appropriate option")

main()    