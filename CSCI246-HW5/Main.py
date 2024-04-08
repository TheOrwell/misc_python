"""
CITATION: Consulted Claude from Antrhopic during the solving of this problem; mostly to ensure the functions
    were created correctly and that the test cases were good.
"""


def inverse(a, n):
    x, y, d = extEuclid(a, n)
    if d == 1:
        return x % n
    else:
        return f"No inverse for a exists in ℤ_{n}"


def extEuclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, r = extEuclid(b, a % b)
        x, y = y, x - (a // b) * y
        return x, y, r


print("Test Case Results: \n")
print(inverse(3, 11))   # When 'a' has an inverse modulo 'n:'
print(inverse(4, 6))    # When 'a' does not have a 'n' inverse.
print(inverse(5, 8))    # When 'a' and 'n' are "coprime."
print(inverse(2, 7))     # When 'n' is a prime number.
