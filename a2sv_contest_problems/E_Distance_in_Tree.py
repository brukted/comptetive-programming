from collections import defaultdict
from functools import cache, lru_cache
from sys import setrecursionlimit, stdin

setrecursionlimit(25_000)

n, k = list(map(int, stdin.readline().split()))

tree = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)


@cache
def canBeRoot(root, parent=-1, depth=k):
    if depth == 0:
        return 1

    if len(tree[root]) == 0:
        return 0

    ans = 0

    for child in tree[root]:
        if child != parent:
            ans += canBeRoot(child, root, depth - 1)

    return ans

ans = 0

for i in range(n):
    ans += canBeRoot(i)

print(ans // 2)
