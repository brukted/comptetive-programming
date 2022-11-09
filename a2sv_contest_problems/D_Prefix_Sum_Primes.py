from collections import Counter
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


n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
ss = sum(arr)
count = Counter(arr)


primes = prime_list(ss)
i = 0
last = 0
ans = []

while ss > 0:
    if count[1] == 0 or count[2] == 0 or i == len(primes):
        ans.extend((1 for _ in range(count[1])))
        ans.extend((2 for _ in range(count[2])))
        break

    if last + 1 == primes[i]:
        ans.append(1)
        count[1] -= 1
        last += 1
    else:
        ans.append(2)
        count[2] -= 1
        last += 2
    
    if last == primes[i]:
        i += 1

print(*ans)