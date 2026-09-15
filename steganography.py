from PIL import Image


# =========================================
# TEXT → BINARY
# =========================================

def text_to_binary(text):
    """Convert text into 8-bit binary."""

    return ''.join(
        format(ord(char), '08b')
        for char in text
    )


# =========================================
# BINARY → TEXT
# =========================================

def binary_to_text(binary):
    """Convert binary back into text."""

    text = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i + 8]

        if len(byte) == 8:
            text += chr(int(byte, 2))

    return text


# =========================================
# ENCODE
# =========================================

def encode_image(input_image, output_image, secret_message):

    image = Image.open(input_image).convert("RGB")

    pixels = list(image.getdata())

    # Convert message to binary
    binary_message = text_to_binary(secret_message)

    # Store message length at the beginning
    message_length = len(binary_message)

    # 32 bits reserved for message length
    header = format(message_length, '032b')

    # Final data
    data = header + binary_message

    # Image capacity
    capacity = len(pixels) * 3

    if len(data) > capacity:

        raise ValueError(
            "Secret message is too large for this image."
        )

    new_pixels = []

    data_index = 0

    for pixel in pixels:

        red, green, blue = pixel

        new_pixel = [
            red,
            green,
            blue
        ]

        for channel in range(3):

            if data_index < len(data):

                # Remove existing LSB
                new_pixel[channel] = (
                    new_pixel[channel] & 254
                )

                # Insert secret bit
                new_pixel[channel] = (
                    new_pixel[channel]
                    | int(data[data_index])
                )

                data_index += 1

        new_pixels.append(
            tuple(new_pixel)
        )

    # Create encoded image
    encoded_image = Image.new(
        "RGB",
        image.size
    )

    encoded_image.putdata(
        new_pixels
    )

    encoded_image.save(
        output_image
    )

    print("Message successfully hidden!")
    print("Output:", output_image)


# =========================================
# DECODE
# =========================================

def decode_image(encoded_image):

    image = Image.open(
        encoded_image
    ).convert("RGB")

    pixels = list(
        image.getdata()
    )

    binary_data = ""

    # Extract all LSBs
    for pixel in pixels:

        red, green, blue = pixel

        binary_data += str(red & 1)
        binary_data += str(green & 1)
        binary_data += str(blue & 1)

    # First 32 bits contain message length
    header = binary_data[:32]

    message_length = int(
        header,
        2
    )

    # Extract only the actual message
    message_binary = binary_data[
        32:32 + message_length
    ]

    # Check whether enough data exists
    if len(message_binary) != message_length:

        raise ValueError(
            "Invalid or corrupted encoded image."
        )

    return binary_to_text(
        message_binary
    )