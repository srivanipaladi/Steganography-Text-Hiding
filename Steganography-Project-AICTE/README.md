# 🕵️‍♂️ Simple Text Steganography using LSB in Images

This Python project hides secret text messages inside images using the **Least Significant Bit (LSB)** technique.

## 🔧 Tools Used
- Python
- Pillow (PIL) library
- PNG format images

## 💻 How It Works

### 1. Encode a Message
- `encode.py` hides a message in a PNG image by modifying the pixel values slightly.
- Output: `encoded.png` which looks the same, but secretly holds the message.

### 2. Decode the Message
- `decode.py` reads the `encoded.png` and extracts the hidden message.

## 📦 Files Included
- `encode.py` – Python code to hide text
- `decode.py` – Python code to retrieve text
- `input.png` – Sample image used
- `encoded.png` – Output image with hidden message

## 🧪 Run Instructions
Install Pillow first:
```bash
pip install pillow
