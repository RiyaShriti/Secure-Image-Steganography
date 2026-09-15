

\# 🔐 Secure Image Steganography



A Python-based image steganography application that allows users to securely hide secret messages inside digital images and extract them when required.



\## 📌 Project Overview



\*\*Secure Image Steganography\*\* is a security-focused project that demonstrates how confidential text can be hidden inside an image without visibly changing its appearance.



The application uses image-processing techniques to encode and decode messages while maintaining image quality. It also provides image-capacity checking and PSNR-based quality evaluation.



\## ✨ Features



\- Hide secret text messages inside images.

\- Extract hidden messages from encoded images.

\- Check whether an image has sufficient capacity for a message.

\- Preserve the visual quality of the original image.

\- Evaluate image quality using Peak Signal-to-Noise Ratio (PSNR).

\- Simple and user-friendly interface using Streamlit.

\- Lightweight and easy to run locally.



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Core programming language |

| Streamlit | Web-based user interface |

| Pillow (PIL) | Image processing |

| NumPy | Numerical and array operations |

| Git \& GitHub | Version control and project hosting |



\## 🧠 How It Works



The project follows a simple encode-and-decode workflow:



1\. The user selects an image.

2\. The user enters a secret message.

3\. The application checks the image's message capacity.

4\. The message is encoded into the image.

5\. The encoded image is saved.

6\. The hidden message can later be extracted using the decode functionality.

7\. PSNR can be used to compare the original and encoded images.



\## 📂 Project Structure



```text

Secure-Image-Steganography/

│

├── app.py                  # Streamlit application

├── encode.py               # Message encoding logic, if applicable

├── decode.py               # Message decoding logic, if applicable

├── requirements.txt        # Required Python libraries

├── README.md               # Project documentation

├── .gitignore              # Ignored files and folders

│

└── assets/                 # Sample images or screenshots, if applicable

```



> Remove `encode.py`, `decode.py`, or `assets/` from this structure if these files do not exist in your project.



\## ⚙️ Installation



\### 1. Clone the Repository



```bash

git clone https://github.com/RiyaShriti/Secure-Image-Steganography.git

```



\### 2. Navigate to the Project Directory



```bash

cd Secure-Image-Steganography

```



\### 3. Create a Virtual Environment



```bash

python -m venv venv

```



\### 4. Activate the Virtual Environment



\*\*Windows PowerShell:\*\*



```powershell

venv\\Scripts\\Activate.ps1

```



\*\*Windows Command Prompt:\*\*



```cmd

venv\\Scripts\\activate

```



\### 5. Install Dependencies



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



Start the Streamlit application using:



```bash

streamlit run app.py

```



The application will open in your browser. If it does not open automatically, copy the local URL displayed in the terminal and open it manually.



\## 🔎 Example Workflow



\### Encoding a Message



1\. Upload an image.

2\. Enter the secret message.

3\. Check the image capacity.

4\. Encode the message.

5\. Download or save the resulting image.



\### Decoding a Message



1\. Upload the encoded image.

2\. Select the decode option.

3\. Extract the hidden message.

4\. Display the recovered text.



\## 📊 Image Quality Evaluation



The project can use \*\*Peak Signal-to-Noise Ratio (PSNR)\*\* to evaluate the difference between the original image and the encoded image.



A higher PSNR value generally indicates that the encoded image is visually closer to the original image.



\## 🔒 Security Note



This project demonstrates image steganography for educational and experimental purposes.



Steganography hides the existence of a message, but it does not automatically provide strong encryption. For highly sensitive information, message encryption should be applied before embedding the message into an image.



\## 🚀 Future Enhancements



\- Add password-based message protection.

\- Encrypt messages before embedding them.

\- Support multiple image formats.

\- Add drag-and-drop image upload.

\- Improve error handling and validation.

\- Add image comparison and PSNR visualization.

\- Deploy the application online.

\- Add automated testing.



\## 🎯 Learning Outcomes



Through this project, the following concepts are practiced:



\- Image processing with Python.

\- File handling and binary data operations.

\- Data hiding and steganography.

\- Numerical computation using NumPy.

\- Image-quality analysis using PSNR.

\- Streamlit application development.

\- Git and GitHub version control.



\## 👩‍💻 Author



\*\*Riya Shriti\*\*



B.Tech Computer Science Engineering  

Specialization: Artificial Intelligence and Machine Learning



GitHub: \[RiyaShriti](https://github.com/RiyaShriti)



\## 📄 License



This project is intended for educational purposes. You may modify and improve it for learning and experimentation.

