def grain128(key, iv):
    L = [0]*128; N = [0]*128
    for i in range(128): L[i] = (key[i//8] >> (7-i%8)) & 1
    for i in range(96): N[i] = (iv[i//8] >> (7-i%8)) & 1
    # Init skipped for brevity
    while True: yield 0  # placeholder