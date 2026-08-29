from steganography import encode_image, decode_image
from crypto import encrypt_message, decrypt_message

from image_metrics import (
    calculate_mse,
    calculate_psnr,
    calculate_ssim,
    get_image_capacity,
    get_message_size
)


# =========================================
# USER DATA
# =========================================

message = "Hello ! This is my secret message."

password = "MySecret123"


# =========================================
# ENCRYPT
# =========================================

encrypted_message = encrypt_message(
    message,
    password
)


# =========================================
# ENCODE
# =========================================

encode_image(
    "sample.png",
    "encoded.png",
    encrypted_message
)


# =========================================
# DECODE
# =========================================

extracted_message = decode_image(
    "encoded.png"
)


# =========================================
# DECRYPT
# =========================================

decrypted_message = decrypt_message(
    extracted_message,
    password
)


# =========================================
# IMAGE QUALITY
# =========================================

mse = calculate_mse(
    "sample.png",
    "encoded.png"
)

psnr = calculate_psnr(mse)

ssim = calculate_ssim(
    "sample.png",
    "encoded.png"
)


# =========================================
# CAPACITY
# =========================================

capacity = get_image_capacity(
    "sample.png"
)


# =========================================
# RESULTS
# =========================================

print("\n==============================")
print("        PROJECT RESULTS")
print("==============================")

print("\nOriginal Message:")
print(message)

print("\nDecoded Message:")
print(decrypted_message)

print("\nImage Capacity:")
print(f"{capacity} bytes")
print(f"{capacity / 1024:.2f} KB")

print("\nImage Quality:")

print(f"MSE  : {mse:.6f}")

print(f"PSNR : {psnr:.2f} dB")

print(f"SSIM : {ssim:.6f}")

print("==============================")

message_size = get_message_size(message)

print("\nMessage Size:")
print(f"{message_size} bytes")
print(f"{message_size / 1024:.2f} KB")


# =========================================
# CAPACITY USAGE
# =========================================

message_size = get_message_size(message)

usage = (
    message_size / capacity
) * 100

# =========================================
# RESULTS
# =========================================

print("\n==============================")
print("        PROJECT RESULTS")
print("==============================")

print("\nOriginal Message:")
print(message)

print("\nDecoded Message:")
print(decrypted_message)

print("\nImage Capacity:")
print(f"{capacity} bytes")
print(f"{capacity / 1024:.2f} KB")

print("\nMessage Size:")
print(f"{message_size} bytes")
print(f"{message_size / 1024:.2f} KB")

print("\nCapacity Used:")
print(f"{usage:.2f}%")

print("\nImage Quality:")

print(f"MSE  : {mse:.6f}")
print(f"PSNR : {psnr:.2f} dB")
print(f"SSIM : {ssim:.6f}")

print("==============================")