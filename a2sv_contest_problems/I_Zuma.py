from functools import lru_cache
from math import inf
from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

jumps = [[] for _ in range(n)]

for i in range(n):
    left, right = i, i
    while left > - 1 and right < n and arr[left] == arr[right]:
        jumps[right].append(right - left + 1)
        left -= 1
        right += 1
    
    left, right = i, i + 1
    while left > - 1 and right < n and arr[left] == arr[right]:
        jumps[right].append(right - left + 1)
        left -= 1
        right += 1


@lru_cache(None)
def solve(i=n - 1):
    if i == -1:
        return 0
    best = inf
    for pos_jum in jumps[i]:
        best = min(best, solve(i - pos_jum) + 1)
    return best


print(solve())
