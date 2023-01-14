'''
Part of EggEngine.

Usage: 'from EggEngine import encrypt' or 'import EggEngine.encrypt'

Includes many useful functions for encryption and decryption of files. Utilizes Fernet from cryptography module.

Made by @eggnaut
'''

import sys
import cryptography.fernet as cr
import files

def generateKey(self) -> bytes:
    '''
    Generates a random key for encryption with Fernet from the cryptography module.

    Returns:
        key (bytes): this is a key that can be used for encryption
    '''
    
    key = cr.Fernet.generate_key()

    return key

def generateKeyFile(file: str) -> None:
    '''
    Generates a random key and stores in file for encryption with Fernet from the cryptography module.

    Args:
        file (str): the path to the file, the key will be stored here
    '''
    
    key = cr.Fernet.generate_key()

    with open(file, 'ab') as keyFile:
        keyFile.write(key)

        keyFile.close()

def loadKey(file: str) -> bytes:
    '''
    Given a file, loads the key to be used for encryption

    Args:
        file (str): the path to the file containing the key

    Returns:
        key (bytes): the key that is contained in the file
    '''
    
    try:
        with open(file, 'rb') as keyFile:
            key = keyFile.read()

        keyFile.close()

        return key

    except FileNotFoundError:
        print(f'\nEggEngine.encrypt.loadKey() was unable to read the file given.\nFileNotFoundError: {file} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit()

def encryptFile(key: bytes, file: str) -> None:
    '''
    Encrypts (into gibberish) a file given a key using Fernet from the cryptography module.
    
    Args:
        key (bytes): the key used for encrypting the file (keep same throughout encryption process)
        file (str): the file you want to encrypt
    '''
    
    fernetObj = cr.Fernet(key)
    try:
        with open(file, 'rb') as originalFile:
            text = originalFile.read()

            originalFile.close()

        encrypted = fernetObj.encrypt(text)

    except FileNotFoundError:
        print(f'\nEggEngine.encrypt.encryptFile() was unable to read the file given.\nFileNotFoundError: {file} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit()

    with open (file, 'wb') as newFile:
        newFile.write(encrypted)

        newFile.close()

def decryptFile(key: bytes, file: str) -> None:
    '''
    Decrypts (into original form) a file givena  key using Fernet from the cryptography module.

    Args:
        key (bytes): the key used for decrypting the file (must be same as encrypting)
        file (str): the file you want to decrypt
    '''
    
    fernetObj = cr.Fernet(key)
    try:
        with open(file, 'rb') as originalFile:
            text = originalFile.read()

            originalFile.close()

        decrypted = fernetObj.decrypt(text)

    except FileNotFoundError:
        print(f'\nEggEngine.encrypt.decryptFile() was unable to read the file given.\nFileNotFoundError: {file} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit()

    with open(file, 'wb') as newFile:
        newFile.write(decrypted)

        newFile.close()