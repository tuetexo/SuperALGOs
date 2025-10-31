def chacha8_block(key, nonce, counter):
    state = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574] + key + [counter] + nonce
    working = state[:]
    for _ in range(4):
        for i in range(0, 16, 4):
            a,b,c,d = i,i+1,i+2,i+3
            working[a] += working[b]; working[d] ^= working[a]; working[d] = (working[d] << 16) | (working[d] >> 16)
            working[c] += working[d]; working[b] ^= working[c]; working[b] = (working[b] << 12) | (working[b] >> 20)
            working[a] += working[b]; working[d] ^= working[a]; working[d] = (working[d] << 8) | (working[d] >> 24)
            working[c] += working[d]; working[b] ^= working[c]; working[b] = (working[b] << 7) | (working[b] >> 25)
    return bytes((state[i] + working[i]) & 0xFF for i in range(16))