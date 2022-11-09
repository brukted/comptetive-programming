from collections import defaultdict
from email.policy import default
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, c = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    orbits = defaultdict(int)
    
    for nn in arr:
        orbits[nn] += 1

    ans = 0
    for val in orbits.values():
        ans += min(val, c)
    
    print(ans)