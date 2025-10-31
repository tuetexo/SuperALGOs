PI = [0xFC,0xEE,0xDD,0x11,0xCF,0x6E,0x31,0x16,0xFB,0xC4,0xFA,0xDA,0x23,0xC5,0x04,0x4D]
def kuznyechik_encrypt(block, key):
    state = list(block)
    K = [key[i*16:(i+1)*16] for i in range(10)]
    for r in range(9):
        for i in range(16): state[i] ^= K[r][i]
        state = [PI[b] for b in state]
        # Simplified linear layer (full L-table omitted for brevity)
    return bytes(state)