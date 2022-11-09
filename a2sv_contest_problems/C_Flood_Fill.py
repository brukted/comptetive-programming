from math import inf
from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

new_arr = [arr[0]]

for ch in arr:
    if ch != new_arr[-1]:
        new_arr.append(ch)

n = len(new_arr)

dp_j_1 = [i + 1 for i in range(n + 1)]
dp_j_1[-1] = 0
dp_j = [None for _ in range(n + 1)]

ans = dp_j_1[n - 2]

for j in range(n - 1, -1, -1):
    dp_j[-1] = n - j

    for i in range(j - 1):
        if new_arr[i] == new_arr[j]:
            dp_j[i] = 1 + dp_j_1[i - 1]
        else:
            dp_j[i] = min(dp_j[i - 1], dp_j_1[i]) + 1

        if i == j - 2:
            ans = min(ans, dp_j[i])

    dp_j, dp_j_1 = dp_j_1, dp_j


print(ans)
