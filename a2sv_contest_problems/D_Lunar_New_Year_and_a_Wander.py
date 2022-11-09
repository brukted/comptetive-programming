from collections import defaultdict
import heapq

n, m = map(int, input().split())

edges = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

ans = []
path = [1]
seen = set()

while path:
    i = heapq.heappop(path)
    seen.add(i)
    ans.append(i)

    for j in edges[i]:
        if j not in seen:
            seen.add(j)
            heapq.heappush(path, j)

print(' '.join(map(str, ans)))
