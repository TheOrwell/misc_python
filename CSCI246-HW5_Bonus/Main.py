def GenerateKeys(p, q):
    # Choosing 2 large primes p and q in method call below
    # Define n == pq
    n = p * q

    # choose an e != 1 so that (p-1) and (q-1) are relatively prime
    relPrime = False
    e = 2  # Choosing an e != 1
    while not relPrime:
        # Check if e is relatively prime with (p-1)*(q-1)
        _, _, gcd = extEuclid(e, (p - 1) * (q - 1))
        if gcd == 1:
            relPrime = True
        else:
            e += 1

    # Compute inverse of e % (p-1)(q-1) and make it equal to d.
    d = inverse(e, (p - 1) * (q - 1))

    # Publish Public key: <e, n> Secret key: <d,n>
    return (e, n), (d, n)


def Encrypt(M, e, n):
    # Compute modular exponentiation using the built-in pow method and return result
    return pow(M, e, n)


def Decrypt(E, d, n):
    # Compute modular exponentiation using the built-in pow method, with adjusted vars for decryption and return result
    return pow(E, d, n)


# inverse function from previous homeworks
def inverse(a, n):
    x, y, d = extEuclid(a, n)
    if d == 1:
        return x % n
    else:
        return f"No inverse for a exists in ℤ_{n}"


# extEuclid function from previous homeworks
def extEuclid(n, m):
    if m % n == 0:
        return 1, 0, n
    else:
        x, y, r = extEuclid(m % n, n)
        return (y - (m // n) * x), x, r


def euclid(n, m):
    if m % n == 0:
        return n
    else:
        return euclid(m % n, n)


# Example from book, run via code:
# Generate keys
p, q = 13, 17
public_key, private_key = GenerateKeys(p, q)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")

# Encrypt message
m = 202
e, n = public_key
encrypted = Encrypt(m, e, n)
print(f"Encrypted message: {encrypted}")

# Decrypt ciphertext
d, n = private_key
decrypted = Decrypt(encrypted, d, n)
print(f"Decrypted message: {decrypted}")