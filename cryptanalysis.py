from brute_force import brute_force
from utils import bits_to_text

def main():
    print("===== Cryptanalysis Tool =====")
    print("1. Brute Force Attack")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        known_phrase = input("Enter known phrase (part of plaintext): ")

        IV = [0,1,0,1,1,0,1,0]
        with open("ciphertext.bin", "rb") as f:
            byte_arr = f.read()

        ciphertext_bits = []
        for byte in byte_arr:
            bits = list(bin(byte)[2:].zfill(8))
            ciphertext_bits.extend([int(b) for b in bits])

        key, plaintext = brute_force(ciphertext_bits, IV, known_phrase)
        if key:
            print("Recovered key:", ''.join(str(b) for b in key))
        else:
            print("Key not found.")

    else:
        print("Exiting.")

if __name__ == "__main__":
    main()
