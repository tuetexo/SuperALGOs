def hummingbird2_encrypt(msg, key, nonce):
    S = [0]*8
    for i in range(8): S[i] = (key[i%16] << 8) | nonce[i%16]
    out = bytearray()
    for m in msg:
        for _ in range(4):
            S[0] ^= S[7]; S[1] ^= S[0]; S[2] ^= S[1]; S[3] ^= S[2]
            S[4] ^= S[3]; S[5] ^= S[4]; S[6] ^= S[5]; S[7] ^= S[6]
        out.append(m ^ (S[0] & 0xFF))
    return bytes(out)