def helix_encrypt(plaintext, key, nonce):
    state = [0]*5
    for i in range(5): state[i] = (key[i%len(key)] << 24) | (nonce[i%len(nonce)] << 16)
    out = bytearray()
    for p in plaintext:
        state[4] = (state[4] + state[0]) & 0xFFFFFFFF
        state[0] = (state[0] ^ p) + state[3]
        out.append(state[4] & 0xFF)
        state = state[1:] + [state[0]]
    return bytes(out)