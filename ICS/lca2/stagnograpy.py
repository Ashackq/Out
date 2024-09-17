import cv2
import numpy as np
import hashlib
from PIL import Image
from PIL import PngImagePlugin


def encrypt_data(data, p, q):
    # Use RSA encryption scheme
    n = p * q
    e = 65537  # Common public exponent
    m = int.from_bytes(data, byteorder="big")  # Convert data to integer
    encrypted = pow(m, e, n)  # RSA encryption: c = m^e mod n
    return encrypted


def decrypt_data(encrypted_data, p, q):
    # Use RSA decryption with CRT optimization
    n = p * q
    e = 65537
    d = pow(e, -1, (p - 1) * (q - 1))  # Private key
    decrypted = pow(encrypted_data, d, n)  # RSA decryption: m = c^d mod n
    decrypted_data = decrypted.to_bytes(
        (decrypted.bit_length() + 7) // 8, byteorder="big"
    )  # Convert back to bytes
    return decrypted_data


def embed_data(image, data):
    # Flatten the image to 1D array
    flat_image = image.flatten()

    # Convert the data to binary format
    binary_data = "".join(format(byte, "08b") for byte in data)

    # Modify the LSBs of the image to embed the binary data
    for i in range(len(binary_data)):
        flat_image[i] = (flat_image[i] & 0xFE) | int(
            binary_data[i]
        )  # Clear LSB and set the new bit

    # Reshape the image back to its original dimensions
    modified_image = flat_image.reshape(image.shape)
    return modified_image


def extract_data(image):
    # Flatten the image to 1D array
    flat_image = image.flatten()

    # Extract the LSBs to recover the binary data
    binary_data = [
        str(flat_image[i] & 1) for i in range(256 * 8)
    ]  # Assuming 256 bytes of data

    # Convert binary data to bytes
    byte_data = bytes(
        [int("".join(binary_data[i : i + 8]), 2) for i in range(0, len(binary_data), 8)]
    )
    return byte_data


def modify_metadata(image_path):
    img = Image.open(image_path)
    metadata = PngImagePlugin.PngInfo()

    # Add or modify metadata
    metadata.add_text("Author", "New Author")
    metadata.add_text("Description", "Modified Image")

    # Save the image with new metadata
    img.save(image_path, pnginfo=metadata)


def check_originality(image_path, original_data, p, q):
    # Read the image
    image = cv2.imread(image_path)

    # Extract data from the image
    extracted_data = extract_data(image)

    # Decrypt the extracted data
    decrypted_data = decrypt_data(extracted_data, p, q)

    # Calculate hashes
    original_hash = hashlib.sha256(original_data).hexdigest()
    extracted_hash = hashlib.sha256(decrypted_data).hexdigest()

    # Compare hashes
    if original_hash == extracted_hash:
        return True  # Original
    else:
        return False  # Tampered


p = 61
q = 53
image_path = "image.jpg"
original_data = b"This is the original data"

# Encrypt data
encrypted_data = encrypt_data(original_data, p, q)

# Embed encrypted data into the image
image = cv2.imread(image_path)
modified_image = embed_data(image, encrypted_data)

# Save modified image
cv2.imwrite("modified_image.jpg", modified_image)

# Modify metadata
modify_metadata("modified_image.jpg")

# Check originality
is_original = check_originality("modified_image.jpg", original_data, p, q)
print("Is original:", is_original)
