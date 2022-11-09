from cmath import inf
from sys import stdin, stdout

n = int(stdin.readline().strip())
cost = list(map(int, stdin.readline().split()))
strings = []
for _ in range(n):
    s = input()
    strings.append([s, s[::-1]])

curr = [("", 0), ("", 0)]
i = 0
while i < n and len(curr) != 0:
    curr_rev_cost = inf
    curr_nor_cost = inf

    for (s, c) in curr:
        if s <= strings[i][0]:
            curr_nor_cost = min(curr_nor_cost, c)
        if s <= strings[i][1]:
            curr_rev_cost = min(curr_rev_cost, c + cost[i])

    curr = []
    if curr_nor_cost != inf:
        curr.append((strings[i][0], curr_nor_cost))
    if curr_rev_cost != inf:
        curr.append((strings[i][1], curr_rev_cost))
    i += 1

ans = inf
if curr:
    ans = min(ans, min(map(lambda x: x[1], curr)))

print(ans if ans != inf else -1)
