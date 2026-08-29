import base64
import hashlib
import os

from cryptography.fernet import Fernet


# =========================================
# SECURITY SETTINGS
# =========================================

ITERATIONS = 600_000
SALT_SIZE = 16


# =========================================
# GENERATE KEY FROM PASSWORD
# =========================================

def generate_key(password, salt):
    """
    Derive a secure encryption key from
    the user's password using PBKDF2.
    """

    password_bytes = password.encode("utf-8")

    key = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt,
        ITERATIONS
    )

    return base64.urlsafe_b64encode(key)


# =========================================
# ENCRYPT MESSAGE
# =========================================

def encrypt_message(message, password):
    """
    Encrypt a message using a password.

    A random salt is generated for every
    encryption operation.
    """

    salt = os.urandom(SALT_SIZE)

    key = generate_key(
        password,
        salt
    )

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        message.encode("utf-8")
    )

    # Store salt + encrypted data
    result = (
        base64.urlsafe_b64encode(salt).decode()
        + ":"
        + encrypted.decode()
    )

    return result


# =========================================
# DECRYPT MESSAGE
# =========================================

def decrypt_message(encrypted_message, password):
    """
    Decrypt a message using the password
    and the salt stored with the ciphertext.
    """

    salt_b64, encrypted_data = (
        encrypted_message.split(":", 1)
    )

    salt = base64.urlsafe_b64decode(
        salt_b64.encode()
    )

    key = generate_key(
        password,
        salt
    )

    cipher = Fernet(key)

    decrypted = cipher.decrypt(
        encrypted_data.encode()
    )

    return decrypted.decode("utf-8")