def skipjack_encrypt(plaintext, key):
    w = [(plaintext >> (16 * i)) & 0xFFFF for i in range(4)]
    key = [k for k in key] + [key[i % len(key)] for i in range(32 - len(key))]
    g = lambda x, k: (x ^ k) % 256
    for r in range(32):
        for i in range(4):
            w[i] = (w[i] ^ g(w[(i-1)%4], key[r])) % 65536
    return sum(w[i] << (16 * i) for i in range(4))