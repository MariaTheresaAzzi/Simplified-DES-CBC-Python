from sdes import key_generation
from cbc_mode import decrypt_cbc
from utils import split_bits_into_blocks, bits_to_text

def load_ciphertext_from_file(filename="ciphertext.bin"):
    with open(filename, "rb") as f:
        byte_arr = f.read()

    ciphertext_bits = []
    for byte in byte_arr:
        bits = list(bin(byte)[2:].zfill(8))
        ciphertext_bits.extend([int(b) for b in bits])
    return ciphertext_bits

def main():
    key_str = input("Enter the 10-bit key (e.g., 1010000010): ")
    key_bits = [int(b) for b in key_str.strip()]
    K1, K2 = key_generation(key_bits)

    IV = [0,1,0,1,1,0,1,0]  # Initialization Vector (must match encryption)

    ciphertext_bits = load_ciphertext_from_file()
    ciphertext_blocks = split_bits_into_blocks(ciphertext_bits, 8)
    decrypted_blocks = decrypt_cbc(ciphertext_blocks, K1, K2, IV)

    decrypted_bits = []
    for block in decrypted_blocks:
        decrypted_bits.extend(block)

    plaintext = bits_to_text(decrypted_bits)
    print("Decrypted plaintext:")
    print(plaintext)

if __name__ == "__main__":
    main()

