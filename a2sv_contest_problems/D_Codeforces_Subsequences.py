from collections import defaultdict
from sys import stdin, stdout

k = int(stdin.readline().strip())

curr = 1
count = defaultdict(lambda: 1)

dss = "codeforces"

while curr < k:
    i = 0

    while curr < k and i < 10:
        # print(curr)
        curr //= count[i]
        count[i] += 1
        curr *= count[i]
        i += 1

for i in range(10):
    for _ in range(count[i]):
        stdout.write(dss[i])

stdout.write('\n')
