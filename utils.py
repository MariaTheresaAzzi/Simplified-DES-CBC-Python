def xor_bits(bits1, bits2):
    return [a ^ b for a, b in zip(bits1, bits2)]

def text_to_bits(text):
    bits = []
    for char in text:
        binval = bin(ord(char))[2:].zfill(8)
        bits.extend([int(b) for b in binval])
    return bits

def bits_to_text(bits):
    chars = []
    for b in range(0, len(bits), 8):
        byte = bits[b:b+8]
        byte_str = ''.join(str(bit) for bit in byte)
        chars.append(chr(int(byte_str, 2)))
    return ''.join(chars)

def split_bits_into_blocks(bits, block_size):
    blocks = []
    for i in range(0, len(bits), block_size):
        block = bits[i:i+block_size]
        if len(block) < block_size:
            block += [0] * (block_size - len(block))  # padding with zeros
        blocks.append(block)
    return blocks
