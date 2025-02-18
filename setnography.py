import cv2

def encrypt_image(img_path, secret_msg, output_path):
    # Read the image
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError("Image not found or invalid image format")
    
    # Add delimiter to mark end of message
    delimiter = "#####"
    full_msg = secret_msg + delimiter
    
    # Convert message to binary
    binary_msg = ''.join([format(ord(i), "08b") for i in full_msg])
    total_bits = len(binary_msg)
    
    # Check if message fits in image
    img_height, img_width = img.shape[0], img.shape[1]
    available_bits = img_height * img_width * 3  # 3 channels per pixel
    if total_bits > available_bits:
        raise ValueError("Message too long for the selected image")
    
    # Embed message in LSBs
    data_index = 0
    for row in img:
        for pixel in row:
            for channel in range(3):  # BGR channels
                if data_index < total_bits:
                    # Modify LSB
                    pixel[channel] = (pixel[channel] & 0xFE) | int(binary_msg[data_index])
                    data_index += 1
                else:
                    break
            if data_index >= total_bits:
                break
        if data_index >= total_bits:
            break
    
    # Save the modified image
    cv2.imwrite(output_path, img)
    print(f"Message encrypted successfully in {output_path}")

def decrypt_image(img_path):
    # Read the encrypted image
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError("Image not found or invalid image format")
    
    # Extract LSBs from all pixels
    binary_data = []
    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_data.append(str(channel & 1))
    
    # Convert binary to string
    all_bits = ''.join(binary_data)
    chars = []
    for i in range(0, len(all_bits), 8):
        byte = all_bits[i:i+8]
        if len(byte) < 8:
            break
        chars.append(chr(int(byte, 2)))
    
    # Find delimiter and extract message
    decoded_msg = ''.join(chars)
    delimiter_pos = decoded_msg.find("#####")
    if delimiter_pos == -1:
        return "No hidden message found or message corrupted"
    
    return decoded_msg[:delimiter_pos]

if __name__ == "__main__":
    print("Image Steganography Tool")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        img_path = input("Enter source image path: ")
        message = input("Enter secret message: ")
        output_path = input("Enter output image path (use PNG format): ")
        encrypt_image(img_path, message, output_path)
    
    elif choice == '2':
        img_path = input("Enter encrypted image path: ")
        result = decrypt_image(img_path)
        print("Decrypted message:", result)
    
    else:
        print("Invalid choice")
