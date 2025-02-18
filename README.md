Image Steganography Tool using OpenCV
This Python program allows you to hide secret messages inside images (steganography) and retrieve them later. It uses the OpenCV library to manipulate image pixels and store your message in the least significant bits (LSBs) of the image. The program has two main functions: encrypting a message into an image and decrypting the message from the image.

How It Works
What is Steganography?
Steganography is the practice of hiding information within another medium, such as an image, without visibly altering it. In this program, the secret message is embedded into the image by modifying the least significant bits of the pixel values. This makes the changes invisible to the human eye.

Key Features:
Encryption: Hide a secret message inside an image.

Decryption: Extract the hidden message from the image.

User-Friendly: Simple command-line interface for easy use.

Supports PNG Format: PNG is recommended because it uses lossless compression, ensuring the hidden message is preserved.

Requirements
To run this program, you need:

Python 3.x installed on your system.

OpenCV library (opencv-python).

You can install OpenCV using pip:

bash
Copy
pip install opencv-python
How to Use
Save the Code:

Save the provided Python code as steganography.py.

Run the Program:

Open a terminal or command prompt and navigate to the folder where steganography.py is saved.

Run the program using Python:

bash
Copy
python steganography.py
Follow the Prompts:

The program will display a menu with two options:

Copy
Image Steganography Tool
1. Encrypt Message
2. Decrypt Message
Enter your choice (1/2):
Option 1: Encrypt Message

Enter the path to the source image (e.g., original.png).

Enter the secret message you want to hide.

Enter the output image path (e.g., encrypted.png). Always use PNG format to avoid losing the hidden message.

The program will create a new image with the hidden message.

Option 2: Decrypt Message

Enter the path to the encrypted image (e.g., encrypted.png).

The program will extract and display the hidden message.

Example Usage
Encrypting a Message
Run the program:

bash
Copy
python steganography.py
Choose option 1 to encrypt.

Provide the following inputs:

Copy
Enter source image path: original.png
Enter secret message: This is a secret!
Enter output image path (use PNG format): encrypted.png
The program will save the encrypted image as encrypted.png.

Decrypting a Message
Run the program:

bash
Copy
python steganography.py
Choose option 2 to decrypt.

Provide the following input:

Copy
Enter encrypted image path: encrypted.png
The program will display the hidden message:

Copy
Decrypted message: This is a secret!
How the Code Works
Encryption Process
The program reads the input image using OpenCV.

It converts the secret message into binary format.

The binary message is embedded into the least significant bits (LSBs) of the image pixels.

A delimiter (#####) is added to mark the end of the message.

The modified image is saved as a new file.

Decryption Process
The program reads the encrypted image using OpenCV.

It extracts the LSBs from each pixel and converts them back into binary data.

The binary data is converted into a string.

The program looks for the delimiter (#####) to identify the end of the message.

The hidden message is displayed.

Important Notes
Use PNG Format: Always use PNG format for the output image to avoid losing the hidden message due to compression (JPEG is not recommended).

Message Length: The maximum message length depends on the size of the image. Larger images can store longer messages.

Delimiter: The program uses ##### as a delimiter to mark the end of the message. Do not include this sequence in your secret message.

Code Structure
encrypt_image(): Handles the encryption of the message into the image.

decrypt_image(): Handles the extraction of the message from the image.

Main Menu: Provides a simple interface for users to choose between encryption and decryption.

Troubleshooting
Image Not Found: Ensure the image path is correct and the image exists.

Message Too Long: If the message is too long for the image, the program will display an error. Use a larger image or shorten the message.

Corrupted Message: If the image is saved in a lossy format (e.g., JPEG), the hidden message may be corrupted. Always use PNG format.

License
This project is open-source and free to use. Feel free to modify and distribute it as needed.
