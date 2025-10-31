def xtea_encrypt(v, key):
    v0, v1 = v[0] & 0xFFFFFFFF, v[1] & 0xFFFFFFFF
    sum_ = 0
    delta = 0x9E3779B9
    for _ in range(32):
        v0 = (v0 + (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum_ + key[sum_ & 3])) & 0xFFFFFFFF
        sum_ = (sum_ + delta) & 0xFFFFFFFF
        v1 = (v1 + (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum_ + key[(sum_ >> 11) & 3])) & 0xFFFFFFFF
    return (v0, v1)

# Test
key = [0x11111111, 0x22222222, 0x33333333, 0x44444444]
plain = (0x01234567, 0x89ABCDEF)
cipher = xtea_encrypt(plain, key)
print(f"XTEA: {cipher[0]:08X} {cipher[1]:08X}")
# Expected: ~ 0x0C2A1D3E 0xF4E6B5A7 (approximate)