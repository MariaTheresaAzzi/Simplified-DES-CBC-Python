# Permutation and S-box tables used in S-DES
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]
IP =  [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2],
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3],
]

def permute(bits, table):
    return [bits[i-1] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def key_generation(key_10bits):
    # P10 permutation
    permuted = permute(key_10bits, P10)
    left, right = permuted[:5], permuted[5:]
    # LS-1
    left1 = left_shift(left, 1)
    right1 = left_shift(right, 1)
    K1 = permute(left1 + right1, P8)
    # LS-2
    left2 = left_shift(left1, 2)
    right2 = left_shift(right1, 2)
    K2 = permute(left2 + right2, P8)
    return K1, K2

def bits_to_int(bits):
    return int(''.join(str(b) for b in bits), 2)

def int_to_bits(x, size):
    return [int(b) for b in bin(x)[2:].zfill(size)]

def sbox_lookup(bits, sbox):
    row = bits[0]*2 + bits[3]
    col = bits[1]*2 + bits[2]
    val = sbox[row][col]
    return int_to_bits(val, 2)

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    # Expansion permutation on right
    expanded = permute(right, EP)
    xor_result = [a ^ b for a,b in zip(expanded, subkey)]
    left4 = xor_result[:4]
    right4 = xor_result[4:]
    s0_bits = sbox_lookup(left4, S0)
    s1_bits = sbox_lookup(right4, S1)
    combined = s0_bits + s1_bits
    p4_result = permute(combined, P4)
    result = [a ^ b for a,b in zip(left, p4_result)]
    return result + right

def switch(bits):
    return bits[4:] + bits[:4]

def encrypt_block(plaintext_8bits, K1, K2):
    bits = permute(plaintext_8bits, IP)
    bits = fk(bits, K1)
    bits = switch(bits)
    bits = fk(bits, K2)
    ciphertext = permute(bits, IP_INV)
    return ciphertext

def decrypt_block(ciphertext_8bits, K1, K2):
    bits = permute(ciphertext_8bits, IP)
    bits = fk(bits, K2)
    bits = switch(bits)
    bits = fk(bits, K1)
    plaintext = permute(bits, IP_INV)
    return plaintext
