from collections import defaultdict
from sys import stdin, stdout

n = int(stdin.readline().strip())

a = {}
in_degree = defaultdict(int)
ids = set()
for _ in range(n):
    u, v = map(int, stdin.readline().split())
    ids.add(u)
    ids.add(v)
    a[u] = v
    in_degree[v] += 1

ans = [None] * n

curr = 0
i = 1
while curr in a and i < n:
    ans[i] = a[curr]
    curr = a[curr]
    i += 2

first = None
for i in ids:
    if in_degree[i] == 0 and i != 0:
        first = i
        break

ans[0] = first

curr = first
i = 2
while curr in a and i < n:
    ans[i] = a[curr]
    curr = a[curr]
    i += 2

print(*ans)
