# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

# Reverse dictionary for decryption
MORSE_CODE_REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Encrypt function
def encrypt(text):
    encrypted_text = ' '.join(MORSE_CODE_DICT[char] for char in text.upper() if char in MORSE_CODE_DICT)
    return encrypted_text

# Decrypt function
def decrypt(morse_code):
    words = morse_code.split("  ")  # Split by double space to separate words
    decrypted_text = []
    for word in words:
        letters = word.split()  # Split by single space to separate characters
        decoded_word = ''.join(MORSE_CODE_REVERSE_DICT[letter] for letter in letters if letter in MORSE_CODE_REVERSE_DICT)
        decrypted_text.append(decoded_word)
    return ' '.join(decrypted_text)

# Main program
while True:
    print("\nChoose an option:")
    print("1. Encrypt text to Morse code")
    print("2. Decrypt Morse code to text")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        text = input("Enter the text to encrypt: ")
        encrypted_text = encrypt(text)
        print("Encrypted Morse code:", encrypted_text)

    elif choice == '2':
        morse_code = input("Enter the Morse code to decrypt (use single spaces between letters and double spaces between words): ")
        decrypted_text = decrypt(morse_code)
        print("Decrypted text:", decrypted_text)

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
