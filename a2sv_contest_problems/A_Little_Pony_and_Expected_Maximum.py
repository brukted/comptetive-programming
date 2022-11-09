from sys import stdin, stdout

m, n = map(int, stdin.readline().split())

ans = 0.0

for i in range(1, m + 1):
    ans += i * ((i / m) ** n - ((i - 1) / m) ** n)

print(ans)
