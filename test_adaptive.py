from adaptive_steganography import (
    encode_adaptive,
    decode_adaptive
)


message = (
    "Hello! This is an adaptive "
    "steganography test."
)


encode_adaptive(
    "sample.png",
    "adaptive_encoded.png",
    message
)


decoded = decode_adaptive(
    "adaptive_encoded.png"
)


print("\nOriginal:")
print(message)

print("\nDecoded:")
print(decoded)
