from collections import Counter
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    mods = map(lambda x: k - x %
               k, map(int, stdin.readline().split()))

    mods = filter(lambda x: x != k, mods)
    mods = Counter(mods)

    if len(mods) == 0:
        print(0)
        continue

    maxx = max(mods.items(), key=lambda x: (x[1], x[0]))

    if maxx[0] == 0:
        print(0)
        continue

    print((maxx[1] - 1) * k + maxx[0] + 1)
