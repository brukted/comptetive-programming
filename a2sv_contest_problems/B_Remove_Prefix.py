from collections import Counter
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    cnt = Counter(arr)
    cc = n
    i = 0
    while i < n and cc != len(cnt):
        cnt[arr[i]] -= 1
        cc -= 1
        if cnt[arr[i]] == 0:
            cnt.pop(arr[i])
        i += 1
    print(i)
    
