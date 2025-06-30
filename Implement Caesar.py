def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Main program
print("=== Caesar Cipher ===")
choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == 'E':
    result = caesar_encrypt(message, shift)
    print("Encrypted message:", result)
elif choice == 'D':
    result = caesar_decrypt(message, shift)
    print("Decrypted message:", result)
else:
    print("Invalid choice!")
