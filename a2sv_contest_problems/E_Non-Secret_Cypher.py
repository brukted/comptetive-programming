from collections import defaultdict
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

i, j = 0, 0
count = defaultdict(int)
ans = 0

while j < n:
    num = -1

    while j < n and count[num] != k:
        count[arr[j]] += 1
        num = arr[j]
        j += 1
    
    while i < j and count[num] == k:
        # print(i, j)
        ans += n - (j - 1)
        count[arr[i]] -= 1
        i += 1

print(ans)

