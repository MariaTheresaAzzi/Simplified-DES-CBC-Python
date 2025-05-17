from sdes import key_generation
from cbc_mode import encrypt_cbc
from utils import text_to_bits, split_bits_into_blocks

def save_ciphertext_to_file(ciphertext_blocks, filename="ciphertext.bin"):
    with open(filename, "wb") as f:
        for block in ciphertext_blocks:
            byte = int(''.join(str(b) for b in block), 2)
            f.write(bytes([byte]))

def main():
    key_str = input("Enter 10-bit key (e.g., 1010000010): ")
    key_bits = [int(b) for b in key_str.strip()]
    K1, K2 = key_generation(key_bits)

    IV = [0,1,0,1,1,0,1,0]  # Initialization Vector
    plaintext = input("Enter plaintext to encrypt: ")

    bits = text_to_bits(plaintext)
    plaintext_blocks = split_bits_into_blocks(bits, 8)
    ciphertext_blocks = encrypt_cbc(plaintext_blocks, K1, K2, IV)
    save_ciphertext_to_file(ciphertext_blocks)

    print("Encryption complete. Ciphertext saved to 'ciphertext.bin'.")

if __name__ == "__main__":
    main()
