from math import inf
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

i = 0
j = 0

cost = 0
best_num, best_cnt = None, -inf

for j in range(n):
    if j > 0:
        cost += abs(arr[j - 1] - arr[j]) * (j - i)

    while cost > k and i < j:
        cost -= abs(arr[i] - arr[j])
        i += 1

    if j - i + 1 > best_cnt:
        best_cnt = j - i + 1
        best_num = arr[j]

print(best_cnt, best_num)
