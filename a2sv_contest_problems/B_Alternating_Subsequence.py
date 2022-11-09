from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, arr = int(stdin.readline().strip()), list(
        map(int, stdin.readline().split()))

    group_best = arr[0]
    sum = 0

    for idx in range(1, n):
        if arr[idx] // int(abs(arr[idx])) == arr[idx - 1] // int(abs(arr[idx - 1])):
            group_best = max(arr[idx], group_best)
        else:
            sum += group_best
            group_best = arr[idx]

    print(sum + group_best)
