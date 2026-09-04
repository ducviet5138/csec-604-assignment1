CIPHER_TEXT = "UJQHLGYJSHZQAKWPUALAFYADGNWAL"

def main():
    for i in range(26):
        decrypted_text = ""
        for char in CIPHER_TEXT:
            decrypted_char = chr((ord(char) - ord('A') + i) % 26 + ord('A'))
            decrypted_text += decrypted_char
        print(f"Shift {i}: {decrypted_text}")

if __name__ == "__main__":
    main()