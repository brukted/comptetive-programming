from sys import stdin, stdout

MOD = 10 ** 9 + 7
t, k = map(int, stdin.readline().split())

limit = k
queries = []

for i in range(t):
    a, b = map(int, stdin.readline().split())
    queries.append((a, b))
    limit = max(limit, b)

limit += 1
factorials = [1] * (limit + 1)

for i in range(1, limit + 1):
    factorials[i] = (factorials[i - 1] * i) % MOD


def modInv(x): return pow(x, -1, MOD)


def nCr(n, r): return (
    factorials[n] * (modInv(factorials[r]) * modInv(factorials[n - r])) % MOD) % MOD


ans = [0] * limit

for i in range(1, limit):
    cc = 0

    for j in range(i // k + 1):
        if i + 1 - k * j > j:
            cc = (cc + nCr(i + 1 - k * j, j)) % MOD
        else:
            cc = (cc + nCr(j, i + 1 - k * j)) % MOD

    ans[i] = (ans[i - 1] + cc) % MOD

for (a, b) in queries:
    a = (ans[b] - ans[a - 1]) % MOD
    print(a)
