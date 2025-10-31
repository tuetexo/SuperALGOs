def rabbit_encrypt(msg, key, iv):
    x = [0]*8; c = [0]*8
    for i in range(8): x[i] = (key[(2*i)%16] << 24) | (key[(2*i+1)%16] << 16)
    for i in range(4): c[i*2] = (key[(i*4+2)%16] << 24) | (key[(i*4+3)%16] << 16)
    out = bytearray()
    for m in msg:
        keystream = (x[0] ^ x[5]) >> 8
        out.append(m ^ (keystream & 0xFF))
        # Simplified update (full version has carry & square)
    return bytes(out)