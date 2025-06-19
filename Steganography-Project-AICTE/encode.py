from PIL import Image

def encode(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # Convert message to binary + end marker
    binary_msg = ''.join(format(ord(char), '08b') for char in message)
    binary_msg += '1111111111111110'  # Special ending sequence

    binary_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[binary_index])
            binary_index += 1
        if binary_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[binary_index])
            binary_index += 1
        if binary_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[binary_index])
            binary_index += 1
        new_pixels.append((r, g, b))

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
    print("✅ Message hidden successfully!")

# 🔽 Example usage
encode("input.png", "Hello AICTE!", "encoded.png")
