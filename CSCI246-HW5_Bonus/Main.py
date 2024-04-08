"""
TODO: Implement RSA encryption and decryption (see page 374 of the textbook).
    This can be encapsulated in three simple functions:

        - GenerateKeys(p, q): returns (d,e), where p and q are different primes and (d, pq) forms the private key and
            (e, pq) is the public key.
        - Encrypt(M, e, pq): returns E, the encrypted version of M (M is an int < pq)
        - Decrypt(E, d, pq): returns M, the decrypted version of E

    Demonstrate your code works on some examples with different primes and messages.

TODO: Extend your code to handle strings.

Code should be well-styled (commenting, spacing, easily run), and uploaded.
Also include a screenshot of the code running.
"""


def generateKeys(p, q):
    print("Method in development")
    # return (d, e)


def encrypt(M, e, pq):
    print("Method in development")
    # return E


def decrypt(E, d, pq):
    print("Method in development")
    # return M


def gcd(m, n):
    return n % m


def euclid(n, m):
    if m % n == 0:
        return n
    else:
        return euclid(m % n, n)


print(euclid(17, 42))
print(euclid(48, 1024))

