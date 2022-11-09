from sys import stdin, stdout
from math import gcd


def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

alg


t = int(stdin.readline().strip())

for _ in range(t):
    a, b, c, d = map(int, stdin.readline().split())

    found = -1, -1
    m = a * b

    for x in range(a + 1, c + 1):
        if gcd(x, m) != 1:
            continue

        inv = modinv(x, m)
        if b < inv <= d:
            found = (x, inv)
            break

    print(found[0], found[1])
