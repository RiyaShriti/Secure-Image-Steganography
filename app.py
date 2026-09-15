import streamlit as st
import tempfile
import os

from steganography import encode_image, decode_image
from crypto import encrypt_message, decrypt_message

from image_metrics import (
    calculate_mse,
    calculate_psnr,
    calculate_ssim,
    get_image_capacity
)


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="Secure Image Steganography",
    page_icon="🔐",
    layout="centered"
)


# =========================================
# TITLE
# =========================================

st.title("🔐 Secure Image Steganography")

st.write(
    "Hide encrypted secret messages inside images "
    "using LSB steganography."
)


# =========================================
# TABS
# =========================================

encode_tab, decode_tab = st.tabs(
    ["🔒 Encode", "🔓 Decode"]
)


# =========================================
# ENCODE TAB
# =========================================

with encode_tab:

    st.header("Hide a Secret Message")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"]
    )

    secret_message = st.text_area(
        "Enter your secret message"
    )

    password = st.text_input(
        "Enter password",
        type="password"
    )

    if st.button("🔒 Encrypt & Hide"):

        if uploaded_image is None:

            st.error("Please upload an image.")

        elif not secret_message:

            st.error("Please enter a secret message.")

        elif not password:

            st.error("Please enter a password.")

        else:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".png"
            ) as temp_input:

                temp_input.write(
                    uploaded_image.getbuffer()
                )

                input_path = temp_input.name


            output_path = "encoded_output.png"


            try:

                # Encrypt message
                encrypted_message = encrypt_message(
                    secret_message,
                    password
                )


                # Encode encrypted message
                encode_image(
                    input_path,
                    output_path,
                    encrypted_message
                )


                # Calculate metrics
                mse = calculate_mse(
                    input_path,
                    output_path
                )

                psnr = calculate_psnr(
                    mse
                )

                ssim = calculate_ssim(
                    input_path,
                    output_path
                )

                capacity = get_image_capacity(
                    input_path
                )


                # Success
                st.success(
                    "Message encrypted and hidden successfully!"
                )


                # Display image
                st.image(
                    output_path,
                    caption="Encoded Image"
                )


                # Metrics
                st.subheader(
                    "📊 Image Analysis"
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "MSE",
                    f"{mse:.6f}"
                )

                col2.metric(
                    "PSNR",
                    f"{psnr:.2f} dB"
                )

                col3.metric(
                    "SSIM",
                    f"{ssim:.6f}"
                )


                # Download
                with open(
                    output_path,
                    "rb"
                ) as file:

                    st.download_button(
                        "⬇️ Download Encoded Image",
                        file,
                        file_name="encoded_image.png",
                        mime="image/png"
                    )


            except Exception as e:

                st.error(
                    f"Error: {e}"
                )


            finally:

                if os.path.exists(
                    input_path
                ):

                    os.remove(
                        input_path
                    )


# =========================================
# DECODE TAB
# =========================================

with decode_tab:

    st.header("Extract Secret Message")

    encoded_image = st.file_uploader(
        "Upload encoded image",
        type=["png"],
        key="decode"
    )

    decode_password = st.text_input(
        "Enter password",
        type="password",
        key="decode_password"
    )


    if st.button("🔓 Extract & Decrypt"):

        if encoded_image is None:

            st.error(
                "Please upload an encoded image."
            )

        elif not decode_password:

            st.error(
                "Please enter the password."
            )

        else:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".png"
            ) as temp_encoded:

                temp_encoded.write(
                    encoded_image.getbuffer()
                )

                encoded_path = temp_encoded.name


            try:

                # Extract encrypted message
                encrypted_message = decode_image(
                    encoded_path
                )


                # Decrypt
                decrypted_message = decrypt_message(
                    encrypted_message,
                    decode_password
                )


                st.success(
                    "Message successfully extracted!"
                )


                st.subheader(
                    "🔐 Secret Message"
                )

                st.info(
                    decrypted_message
                )


            except Exception:

                st.error(
                    "Unable to decrypt. "
                    "Check the image and password."
                )


            finally:

                if os.path.exists(
                    encoded_path
                ):

                    os.remove(
                        encoded_path
                    )