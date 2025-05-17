from sdes import key_generation
from cbc_mode import decrypt_cbc
from utils import split_bits_into_blocks, bits_to_text

def brute_force(ciphertext_bits, IV, known_phrase):
    for key_int in range(1024):  # all 10-bit keys
        key_bits = [int(b) for b in bin(key_int)[2:].zfill(10)]
        K1, K2 = key_generation(key_bits)
        ciphertext_blocks = split_bits_into_blocks(ciphertext_bits, 8)
        try:
            decrypted_blocks = decrypt_cbc(ciphertext_blocks, K1, K2, IV)
            decrypted_bits = []
            for block in decrypted_blocks:
                decrypted_bits.extend(block)
            decrypted_text = bits_to_text(decrypted_bits)

            # Check if known phrase appears in decrypted text
            if known_phrase in decrypted_text:
                print(f"Key found: {''.join(str(b) for b in key_bits)}")
                print("Decrypted text:")
                print(decrypted_text)
                return key_bits, decrypted_text
        except Exception as e:
            # In case of error just skip this key
            continue
    print("No key found!")
    return None, None

def main():
    IV = [0,1,0,1,1,0,1,0]  # Same IV used for encryption
    known_phrase = input("Enter a known phrase to find in decrypted text: ")

    with open('ciphertext.bin', 'rb') as f:
        byte_arr = f.read()

    ciphertext_bits = []
    for byte in byte_arr:
        bits = list(bin(byte)[2:].zfill(8))
        ciphertext_bits.extend([int(b) for b in bits])

    brute_force(ciphertext_bits, IV, known_phrase)

if __name__ == "__main__":
    main()
