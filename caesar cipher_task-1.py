#Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm.
#Allow users to input a message and a shift value to perform encryption and decryption.
def encrupt(text,s):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters and ord is used to find the ASCII value
        # and chr is used to convert ASCII value back to character
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result
def decrypt(text,s):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char

    return result

# ====== main program ======
choice= input("Do you want to encrypt or decrypt? (E/D): ").lower().upper()
if choice == 'E':
    text = input("Enter the text to encrypt: ")
    s = int(input("Enter the shift value (1-25): "))
    encrypted_text = encrupt(text, s)
    print("Encrypted text:", encrypted_text)
elif choice == 'D':
    text = input("Enter the text to decrypt: ")
    s = int(input("Enter the shift value (1-25): "))
    decrypted_text = decrypt(text, s)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
# This program implements a Caesar cipher for encryption and decryption.
# The user can choose to encrypt or decrypt a message by providing a shift value.
# The program handles both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.
# The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of places down or up the alphabet.
# The shift value must be between 1 and 25.
# The program prompts the user for input and displays the result accordingly.
# The Caesar cipher is named after Julius Caesar, who used it to communicate with his generals.
# The encryption and decryption functions use ASCII values to perform the character shifting.
# The program is case-sensitive, meaning it treats uppercase and lowercase letters differently.      
