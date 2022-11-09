from functools import lru_cache
from heapq import heapify, heappop, heappush
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
string = stdin.readline().strip()
compressed = []
count = 0
curr = string[0]

for ch in string:
    if ch == curr:
        count += 1
    else:
        compressed.append((curr, count))
        curr = ch
        count = 1

compressed.append((curr, count))
suffix_count = [0 for _ in range(len(compressed))]
suffix_count[-1] = compressed[-1][1]

for i in range(len(compressed) - 2, -1, -1):
    suffix_count[i] = suffix_count[i + 1] + compressed[i][1]

visited = {(-target, 0, "") for target in range(n, -1, -1)}
queue = [(-target, 0, "") for target in range(n, -1, -1)]
heapify(queue)

ans = 0
count = 0

while queue and count < k:
    # print(queue)
    target, i, curr = heappop(queue)
    target *= -1
    i *= -1

    rem = target - len(curr)

    if rem == 0 and i == len(compressed):
        count += 1
        ans += n - len(curr)
        # print(curr)

    if i == len(compressed) or suffix_count[i] < rem:
        continue

    ch, curr_count = compressed[i]
    for taken in range(0, min(rem, curr_count) + 1):

        key = (-target, -(i + 1), curr + (ch * taken))

        if key not in visited:
            visited.add(key)
            heappush(queue, key)

print(ans if count == k else -1)
