def katan32_encrypt(plain, key):
    L1, L2 = (plain >> 19) & 0xFFF, plain & 0x7FFFF
    ka, kb = key >> 40, key & 0xFFFFFFFFFF
    for r in range(254):
        fb = L1[0] ^ L1[4] ^ (L1[12] & L1[18]) ^ ka[r % 80]
        L1, L2 = (L1 >> 1) | (fb << 11), (L2 >> 1) | (L1[0] << 18)
    return (L1 << 19) | L2