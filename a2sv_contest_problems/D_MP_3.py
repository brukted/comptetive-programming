from sys import stdin, stdout
from collections import Counter
from math import ceil, log2

n, i = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))


def solveK(n, i):
    l, r = 1, n
    ans = None

    while l <= r:
        mid = (l + r) // 2
        val = ceil(log2(mid)) * n
        
        if val <= i:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


count = list(Counter(arr).items())
count.sort()
count = list(map(lambda x: x[1], count))
i *= 8

K = solveK(n, i)
# can afford all
if K >= len(count):
    print('0')
    exit()
best = sum(count[:K])
s = best
for i in range(K, len(count)):
    s += count[i]
    s -= count[i - K]
    best = max(s, best)

print(n - best)
