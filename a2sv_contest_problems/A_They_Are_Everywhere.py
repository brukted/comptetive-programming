from math import inf
from collections import defaultdict
from sys import stdin, stdout

n = int(stdin.readline().strip())
s = stdin.readline().strip()
typs = len(set(s))

left = right = 0
count = defaultdict(int)
curr_types = 0
ans = inf

for left in range(n):
    while right < n and curr_types != typs:
        if count[s[right]] == 0:
            curr_types += 1
        count[s[right]] += 1
        right += 1

    if curr_types != typs:
        break

    ans = min(ans, right - left)

    if count[s[left]] == 1:
        curr_types -= 1

    count[s[left]] -= 1

print(ans)
