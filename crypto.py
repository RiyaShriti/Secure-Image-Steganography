import base64
import hashlib

from cryptography.fernet import Fernet


def generate_key(password):
    """
    Convert the user's password into a Fernet-compatible key.
    """

    password_bytes = password.encode("utf-8")

    hash_value = hashlib.sha256(
        password_bytes
    ).digest()

    key = base64.urlsafe_b64encode(
        hash_value
    )

    return key


def encrypt_message(message, password):
    """
    Encrypt the secret message using the password.
    """

    key = generate_key(password)

    cipher = Fernet(key)

    encrypted_message = cipher.encrypt(
        message.encode("utf-8")
    )

    return encrypted_message.decode("utf-8")


def decrypt_message(encrypted_message, password):
    """
    Decrypt the encrypted message.
    """

    key = generate_key(password)

    cipher = Fernet(key)

    decrypted_message = cipher.decrypt(
        encrypted_message.encode("utf-8")
    )

    return decrypted_message.decode("utf-8")