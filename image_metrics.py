from PIL import Image
import numpy as np

from skimage.metrics import structural_similarity


def calculate_mse(original_path, encoded_path):
    """
    Calculate Mean Squared Error between
    original and encoded images.
    """

    original = np.array(
        Image.open(original_path).convert("RGB"),
        dtype=np.float64
    )

    encoded = np.array(
        Image.open(encoded_path).convert("RGB"),
        dtype=np.float64
    )

    mse = np.mean(
        (original - encoded) ** 2
    )

    return mse


def calculate_psnr(mse):
    """
    Calculate Peak Signal-to-Noise Ratio.
    """

    if mse == 0:
        return float("inf")

    max_pixel = 255.0

    psnr = 10 * np.log10(
        (max_pixel ** 2) / mse
    )

    return psnr


def calculate_ssim(original_path, encoded_path):
    """
    Calculate Structural Similarity Index.
    """

    original = np.array(
        Image.open(original_path).convert("RGB")
    )

    encoded = np.array(
        Image.open(encoded_path).convert("RGB")
    )

    ssim = structural_similarity(
        original,
        encoded,
        channel_axis=2,
        data_range=255
    )

    return ssim


def get_image_capacity(image_path):
    """
    Calculate approximate LSB capacity in bytes.
    """

    image = Image.open(image_path).convert("RGB")

    width, height = image.size

    capacity_bits = width * height * 3

    capacity_bytes = capacity_bits // 8

    return capacity_bytes

def get_message_size(message):

    return len(
        message.encode("utf-8")
    )