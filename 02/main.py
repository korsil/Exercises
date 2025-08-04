import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt_message(message: str, key: bytes | str) -> str:
    fernet = Fernet(key)
    return fernet.encrypt(message)


def decrypt_message(encrypted_message: str, key: bytes | str) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message)


def main():
    message = b"Ducks will invade Mars"
    password = b"ducksAreSupreme"
    salt = b"SeaWater"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print("Original message:", message)

    encrypted_message = encrypt_message(message, key)
    print("Encrypted message", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message", decrypted_message)



if __name__ == "__main__":
    main()
