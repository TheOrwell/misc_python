"""
CITATION: Consulted Claude from Antrhopic during the solving of this problem. Along with this, the textbook:
    "Connecting Discrete Mathematics and Computer Science" by "David Liben-Nowell" was also consulted, for some good
    test cases of the "extEuclid" and "inverse" methods.
"""


def inverse(a, n):
    x, y, d = extEuclid(a, n)
    if d == 1:
        return x % n
    else:
        return f"No inverse for a exists in ℤ_{n}"


def extEuclid(n, m):
    if m % n == 0:
        return 1, 0, n
    else:
        x, y, r = extEuclid(m % n, n)
        return (y - (m // n) * x), x, r


print("Extended-Euclid computations from book:")
print(extEuclid(12, 18))
print(extEuclid(18, 30))

print("\nMultiplicative Inverse computations from book:")
print(inverse(2, 9))
print(inverse(7, 11))
print(inverse(3, 9))

print("\nMultiplicative Inverse computations for Exercise 7.91:")
print(inverse(7, 15))
