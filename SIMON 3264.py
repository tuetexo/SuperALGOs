def simon_encrypt(plain, key):
    x, y = plain >> 16, plain & 0xFFFF
    k = [key & 0xFFFF]
    for i in range(31): k.append(k[-1] ^ ((k[-1] << 1) | (k[-1] >> 15)) ^ 0xFF00)
    for r in range(32):
        t = ((x << 1) | (x >> 15)) & 0xFFFF
        t ^= ((x << 8) | (x >> 8)) & 0xFFFF
        t ^= y ^ k[r]
        y = x; x = t
    return (x << 16) | y