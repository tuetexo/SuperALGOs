def speck_round(x, y, k):
    x = ((x >> 8) | (x << 8)) & 0xFFFF
    x = (x + y) & 0xFFFF
    x ^= k
    y = (y << 3) | (y >> 13)
    y ^= x
    return x, y
def speck_encrypt(plain, key):
    x, y = plain >> 16, plain & 0xFFFF
    k = [key & 0xFFFF]
    for i in range(21): k.append((k[-1] + (3+i)) & 0xFFFF ^ (k[-1] >> 14))
    for r in range(22): x, y = speck_round(x, y, k[r])
    return (x << 16) | y