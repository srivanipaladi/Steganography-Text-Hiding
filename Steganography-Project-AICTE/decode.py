from PIL import Image

def decode(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    binary_msg = ''
    for pixel in pixels:
        for color in pixel:
            binary_msg += str(color & 1)
            if binary_msg.endswith('1111111111111110'):
                binary_msg = binary_msg[:-16]
                message = ''
                for i in range(0, len(binary_msg), 8):
                    byte = binary_msg[i:i+8]
                    message += chr(int(byte, 2))
                print("🔓 Hidden message:", message)
                return
    print("⚠️ No hidden message found.")

# 🔽 Example usage
decode("encoded.png")

