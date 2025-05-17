from sdes import encrypt_block, decrypt_block

def xor_bits(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def encrypt_cbc(plaintext_blocks, K1, K2, IV):
    ciphertext_blocks = []
    prev_cipher = IV
    for block in plaintext_blocks:
        xor_input = xor_bits(block, prev_cipher)
        cipher_block = encrypt_block(xor_input, K1, K2)
        ciphertext_blocks.append(cipher_block)
        prev_cipher = cipher_block
    return ciphertext_blocks

def decrypt_cbc(ciphertext_blocks, K1, K2, IV):
    plaintext_blocks = []
    prev_cipher = IV
    for block in ciphertext_blocks:
        decrypted = decrypt_block(block, K1, K2)
        plaintext_block = xor_bits(decrypted, prev_cipher)
        plaintext_blocks.append(plaintext_block)
        prev_cipher = block
    return plaintext_blocks

