def trivium(key, iv):
    s = [0]*288
    for i in range(80): s[i] = (key[i//8] >> (7 - i%8)) & 1
    for i in range(80): s[93 + i] = (iv[i//8] >> (7 - i%8)) & 1
    s[285:288] = [1,1,1]
    for _ in range(4*288):  # init
        t1 = s[65] ^ s[92]
        t2 = s[161] ^ s[176]
        t3 = s[242] ^ s[287]
        s = [0] + s[:-1]
        s[0] = t3; s[93] ^= t1; s[177] ^= t2; s[288] ^= t3
    while True:
        yield s[65] ^ s[92] ^ s[161] ^ s[176] ^ s[242] ^ s[287]