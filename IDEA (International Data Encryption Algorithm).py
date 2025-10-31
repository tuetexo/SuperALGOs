def idea_encrypt(block, key):
    def mul(a, b): return ((a * b) % 65537) if a and b else (1 - a - b) % 65537
    X = [(block >> (16*i)) & 0xFFFF for i in range(4)]
    K = [key[i:i+6] for i in range(0, 48, 6)] + [key[:4]]
    for r in range(8):
        X[0] = mul(X[0], K[r][0])
        X[1] = (X[1] + K[r][1]) & 0xFFFF
        X[2] = (X[2] + K[r][2]) & 0xFFFF
        X[3] = mul(X[3], K[r][3])
        t0 = mul(X[0] ^ X[2], K[r][4])
        t1 = mul((X[1] ^ X[3]) + t0 & 0xFFFF, K[r][5])
        X[0] ^= t1; X[1] ^= t0; X[2] ^= t1; X[3] ^= t0
        X[1], X[2] = X[2], X[1]
    X[0] = mul(X[0], K[8][0]); X[1] = (X[1] + K[8][1]) & 0xFFFF
    X[2] = (X[2] + K[8][2]) & 0xFFFF; X[3] = mul(X[3], K[8][3])
    return sum(X[i] << (16*i) for i in range(4))