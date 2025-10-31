def rc5_encrypt(plain, key):
    # RC5-32/12/16 parameters
    w, r, b = 32, 12, 16
    P = 0xB7E15163
    Q = 0x9E3779B9
    MOD = 1 << w

    # Key schedule
    L = [(key[i*4:i*4+4][::-1].hex(), 16) for i in range(b//4)]
    L += [0] * (-b//4)
    S = [P]
    for i in range(1, 2*r + 4):
        S.append((S[-1] + Q) % MOD)

    i = j = 0
    A = B = 0
    for _ in range(3 * max(len(S), len(L))):
        A = S[i] = ((S[i] + A + B) << 3) % MOD
        B = L[j] = ((L[j] + A + B) << (A + B)) % MOD
        i, j = (i + 1) % len(S), (j + 1) % len(L)

    # Encrypt
    A = (plain[0] + S[0]) % MOD
    B = (plain[1] + S[1]) % MOD
    for i in range(1, r + 1):
        A = ((A ^ B) << B) % MOD + S[2*i]
        B = ((B ^ A) << A) % MOD + S[2*i + 1]
    return A, B

# Test
key_bytes = bytes.fromhex("00112233445566778899AABBCCDDEEFF")
key_ints = [int.from_bytes(key_bytes[i:i+4], 'little') for i in range(0, 16, 4)]
plain = (0x01234567, 0x89ABCDEF)
cipher = rc5_encrypt(plain, key_ints)
print(f"RC5: {cipher[0]:08X} {cipher[1]:08X}")
# Known test vector (RC5-32/12/16): 0x2A0C7E1F 0x2D0F1E2D