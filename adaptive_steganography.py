from PIL import Image
import numpy as np


END_MARKER = "1111111111111110"


def text_to_binary(text):
    """Convert text into 8-bit binary."""

    binary = ""

    for char in text:
        binary += format(
            ord(char),
            "08b"
        )

    return binary


def calculate_complexity(image):
    """
    Calculate a simple local complexity score
    using neighboring pixel differences.
    """

    array = np.array(
        image.convert("L"),
        dtype=np.int16
    )

    horizontal = np.abs(
        array[:, 1:] - array[:, :-1]
    )

    vertical = np.abs(
        array[1:, :] - array[:-1, :]
    )

    complexity = np.zeros_like(
        array,
        dtype=np.float64
    )

    complexity[:, 1:] += horizontal
    complexity[1:, :] += vertical

    return complexity


def encode_adaptive(
    input_image,
    output_image,
    secret_message
):
    """
    Hide a message using adaptive LSB embedding.
    """

    image = Image.open(
        input_image
    ).convert("RGB")

    pixels = np.array(
        image,
        dtype=np.uint8
    )

    binary_message = (
        text_to_binary(secret_message)
        + END_MARKER
    )

    complexity = calculate_complexity(
        image
    )

    # Flatten pixels and complexity
    height, width, _ = pixels.shape

    pixel_indices = np.arange(
        height * width
    )

    complexity_flat = complexity.flatten()

    # Sort pixels from highest to lowest complexity
    sorted_indices = pixel_indices[
        np.argsort(
            complexity_flat
        )[::-1]
    ]

    capacity = (
        len(sorted_indices) * 3
    )

    if len(binary_message) > capacity:

        raise ValueError(
            "Secret message is too large "
            "for this image."
        )

    data_index = 0

    for index in sorted_indices:

        row = index // width
        col = index % width

        for channel in range(3):

            if data_index >= len(
                binary_message
            ):
                break

            bit = int(
                binary_message[data_index]
            )

            # Clear LSB
            pixels[row, col, channel] &= 254

            # Insert secret bit
            pixels[row, col, channel] |= bit

            data_index += 1

        if data_index >= len(
            binary_message
        ):
            break

    encoded_image = Image.fromarray(
        pixels
    )

    encoded_image.save(
        output_image
    )

    print(
        "Adaptive message successfully hidden!"
    )

    print(
        "Output:",
        output_image
    )


def decode_adaptive(encoded_image):
    """
    Extract an adaptively embedded message.
    """

    image = Image.open(
        encoded_image
    ).convert("RGB")

    pixels = np.array(
        image,
        dtype=np.uint8
    )

    complexity = calculate_complexity(
        image
    )

    height, width, _ = pixels.shape

    pixel_indices = np.arange(
        height * width
    )

    complexity_flat = complexity.flatten()

    sorted_indices = pixel_indices[
        np.argsort(
            complexity_flat
        )[::-1]
    ]

    binary_data = ""

    for index in sorted_indices:

        row = index // width
        col = index % width

        for channel in range(3):

            bit = pixels[
                row,
                col,
                channel
            ] & 1

            binary_data += str(bit)

            if binary_data.endswith(
                END_MARKER
            ):

                binary_data = binary_data[
                    :-len(END_MARKER)
                ]

                message = ""

                for i in range(
                    0,
                    len(binary_data),
                    8
                ):

                    byte = binary_data[
                        i:i + 8
                    ]

                    if len(byte) == 8:

                        message += chr(
                            int(byte, 2)
                        )

                return message

    raise ValueError(
        "No hidden message found."
    )