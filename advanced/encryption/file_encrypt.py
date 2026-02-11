#!/usr/bin/env python3

import os

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_file(filename, shift):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    encrypted_content = caesar_encrypt(content, shift)

    new_filename = f"{filename}.enc"

    with open(new_filename, "w", encoding="utf-8") as file:
        file.write(encrypted_content)

    print(f"File encrypted successfully!")
    print(f"Encrypted file saved as: {new_filename}")


def decrypt_file(filename, shift):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    decrypted_content = caesar_decrypt(content, shift)

    new_filename = filename.replace(".enc", ".dec")

    with open(new_filename, "w", encoding="utf-8") as file:
        file.write(decrypted_content)

    print("File decrypted successfully!")
    print(f"Decrypted file saved as: {new_filename}")

def main():
    print("Simple File Encryption Tool")
    print("=" * 35)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            filename = input("Enter file name or path to encrypt: ").strip()
            try:
                shift = int(input("Enter encryption key (number): "))
                encrypt_file(filename, shift)
            except ValueError:
                print("Key must be a number.")

        elif choice == "2":
            filename = input("Enter file name or path to decrypt: ").strip()
            try:
                shift = int(input("Enter decryption key (same number used for encryption): "))
                decrypt_file(filename, shift)
            except ValueError:
                print("Key must be a number.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()
