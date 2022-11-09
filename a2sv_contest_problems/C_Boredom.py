from collections import Counter
from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
c = list(Counter(arr).items())
c.sort()

dp = [None] * (len(c) + 1)
dp[-1] = 0
dp[-2] = c[-1][0] * c[-1][1]

for idx in range(len(c) - 2, -1, -1):
    dp[idx] = 0
    val, cnt = c[idx]

    if c[idx + 1][0] != val + 1:
        dp[idx] = (val * cnt) + dp[idx + 1]
    else:
        dp[idx] = max(val * cnt + dp[idx + 2], dp[idx + 1])

print(max(dp))
