from math import inf
from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))


best = [[inf for _ in range(n + 1)] for _ in range(2)]

heap = [(0, 1, 0)]

while heap:
    distance, node, direction = heappop(heap)
    if distance > best[direction][node]:
        continue

    if direction == 0:
        for (nei, w) in graph[node]:
            if w + distance < best[direction][nei]:
                heappush(heap, (w + distance, nei, direction))
                best[direction][nei] = w + distance

    for (nei, w) in reverse_graph[node]:
        if w + distance < best[1][nei]:
            heappush(heap, (w + distance, nei, 1))
            best[1][nei] = w + distance


print(*map(lambda x: min(best[0][x], best[1][x])
      if min(best[0][x], best[1][x]) != inf else -1, range(2, n + 1)))
