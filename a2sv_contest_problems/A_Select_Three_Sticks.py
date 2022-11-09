from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    arr.sort()

    ans = inf

    for i in range(n - 2):
        # make equal to first
        cost = abs(arr[i] - arr[i + 1]) + abs(arr[i] - arr[i + 2])
        cost = min(cost, abs(arr[i] - arr[i + 1]) +
                   abs(arr[i + 1] - arr[i + 2]))
        cost = min(cost, abs(arr[i] - arr[i + 2]) +
                   abs(arr[i + 1] - arr[i + 2]))
        
        ans = min(cost, ans)
    print(ans)
