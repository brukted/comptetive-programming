from collections import defaultdict
from functools import lru_cache
from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
satisfaction = list(map(int, stdin.readline().split()))
transition_gain = defaultdict(int)

for _ in range(k):
    x, y, c = map(int, stdin.readline().split())
    transition_gain[(x - 1, y - 1)] = c


@lru_cache(None)
def solve(seen, seen_count, curr):
    if seen_count == m:
        return satisfaction[curr]

    ans = 0

    for i in range(n):
        if seen & 1 << i:
            continue

        ans = max(
            ans, solve(seen | 1 << i, seen_count + 1, i) + transition_gain[(curr, i)]
        )

    return ans + satisfaction[curr]


print(max(map(lambda i: solve(1 << i, 1, i), range(n))))
