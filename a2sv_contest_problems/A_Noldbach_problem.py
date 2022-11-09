from sys import stdin, stdout


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 +
                   (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res


n, k = map(int, stdin.readline().split())
primes = prime_list(n)
primes_set = set(primes)
count = 0
i = 1

while i < len(primes) and count < k:
    if primes[i] + primes[i - 1] + 1 in primes_set:
        count += 1
        if count >= k:
            break
    i += 1

print("YES" if count >= k else "NO")
