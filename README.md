Complete Project Guide: S-DES with CBC Mode

🔐 Project Objective
Implement Simplified DES (S-DES) encryption and decryption from scratch in Python.

Use CBC (Cipher Block Chaining) mode as the block cipher mode of operation.

Encrypt and decrypt a plaintext file (text, image, or any file).

Perform cryptanalysis (e.g., brute force) to decrypt ciphertext without the key.

Attempt to decrypt another group’s ciphertext by finding their key.

Prepare a detailed report, code, readme, and class presentation.

📚 Step 1: Research
1. Understand S-DES
S-DES is a simplified version of DES designed for educational purposes.

Works on 8-bit plaintext blocks and uses a 10-bit key.

Main components:

Key generation: Derive two 8-bit subkeys (K1 and K2) from the 10-bit key using permutation and shifts.

Initial Permutation (IP) and Inverse IP on the 8-bit plaintext.

Feistel function with expansion/permutation (EP), substitution boxes (S-boxes), and permutation (P4).

Two rounds of processing with subkeys.

Encryption: IP → round 1 with K1 → switch halves → round 2 with K2 → Inverse IP.

Decryption: Same as encryption but use keys in reverse order (K2 then K1).

2. Understand CBC Mode
CBC operates on blocks, XORing each plaintext block with the previous ciphertext block before encryption.

Requires an Initialization Vector (IV) for the first block.

Improves security by making identical plaintext blocks encrypt differently.

Padding is needed if plaintext size is not a multiple of block size (8 bits).

3. Cryptanalysis and Brute Force
Since the keyspace for S-DES is small (2^10 = 1024 keys), brute forcing all keys is feasible.

Known-plaintext attack: If part of the plaintext is known, test all keys to find which produces matching ciphertext.

Ciphertext-only attack: More challenging but possible with statistical analysis or brute force.