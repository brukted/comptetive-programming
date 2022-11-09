from collections import defaultdict
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    ss = defaultdict(int)
    ans = 0

    for i in range(n):
        ans += ss[arr[i] - i]
        ss[arr[i] - i] += 1

    print(ans)
