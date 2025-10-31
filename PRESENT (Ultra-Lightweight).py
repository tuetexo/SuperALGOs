SBOX = [0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]
P = [0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51]
def present_encrypt(plain, key):
    state = plain
    for r in range(31):
        state = [(state >> (4*i)) & 0xF for i in range(16)]
        state = [SBOX[b] for b in state]
        state = sum((state[P[i]] << (4*i)) for i in range(64)) & ((1<<64)-1)
        state ^= key[r % 10]
    return state