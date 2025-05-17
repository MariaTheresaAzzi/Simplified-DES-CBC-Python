# 🔐 S-DES with CBC Mode – Cryptography Project

This project implements the Simplified Data Encryption Standard (S-DES) with **Cipher Block Chaining (CBC)** mode in Python. It demonstrates key cryptographic concepts, including symmetric key encryption, block cipher chaining, and brute-force cryptanalysis.

---

## 📁 Project Structure

```plaintext
.
├── sdes.py            # Core S-DES algorithm: encryption, decryption, key generation
├── cbc_mode.py        # Implements CBC mode using the S-DES cipher
├── encrypt.py         # Encrypts a plaintext file using a user-provided key and IV
├── decrypt.py         # Decrypts a ciphertext using the correct key
├── brute_force.py     # Performs brute-force cryptanalysis to discover the key
├── utils.py           # Helper functions for bitwise operations, padding, and conversions
├── plaintext.txt      # Input plaintext file to encrypt
├── ciphertext.bin     # Output encrypted binary file
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.6+
* No external libraries are required (only standard Python modules)

### 🛠️ Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/S-DES-CBC-Project.git
   cd S-DES-CBC-Project
   ```

2. Ensure `plaintext.txt` exists in the project directory with the message you want to encrypt.

---

## 🔒 How to Encrypt

Run the `encrypt.py` script and input a **10-bit key** and **8-bit IV** when prompted:

```bash
python encrypt.py
```

Example input:

```
Enter 10-bit key (e.g. 1010000010): 
Enter 8-bit IV (e.g. 10101010): 
```

Output: `ciphertext.bin`

---

## 🔓 How to Decrypt

Run the `decrypt.py` script and input the same key and IV used for encryption:

```bash
python decrypt.py
```

Output: Decrypted plaintext printed to the console.

---

## 🧠 Brute-Force Cryptanalysis

Use `brute_force.py` to simulate an attack by trying all possible 10-bit keys.

```bash
python brute_force.py
```

Input a known substring (e.g., `Hello`) from the original plaintext. The script will brute-force decrypt the ciphertext and return the correct key when it finds the known phrase.

---

## 🧪 CBC Mode Logic

CBC mode chains plaintext blocks by XORing each with the previous ciphertext block before encryption:

```
C₁ = E(P₁ ⊕ IV)
C₂ = E(P₂ ⊕ C₁)
...
```

Where:

* `P` = Plaintext block
* `C` = Ciphertext block
* `E()` = Encryption function
* `IV` = Initialization Vector

Implemented in `cbc_mode.py`.

---

## 📚 Educational Objectives

This project was developed as a cryptography assignment to:

1. Understand and implement S-DES from scratch.
2. Explore CBC operation mode for block ciphers.
3. Demonstrate cryptanalysis through brute-force attacks.
4. Reflect on the security limitations of small key sizes.

---

## ⚠️ Disclaimer

This project is **for educational purposes only**. S-DES is **not secure** and should **never** be used in real-world applications.

---

## ✍️ Author

Maria Theresa Azzi

---

Let me know if you'd like to include diagrams or usage examples with screenshots.
