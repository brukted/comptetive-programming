from collections import defaultdict
from heapq import heapify, heappop, heappush
from sys import stdin

n, m = map(int, stdin.readline().split())

reverse_graph = defaultdict(list)
out_degree = {node: 0 for node in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    reverse_graph[v].append(u)
    out_degree[u] += 1

heap = [(-node) for node in range(1, n + 1) if out_degree[node] == 0]
val = n

heapify(heap)

ans = [None for _ in range(n)]
while heap:
    node = -heappop(heap)
    ans[node - 1] = val
    val -= 1

    for par in reverse_graph[node]:
        out_degree[par] -= 1
        if out_degree[par] == 0:
            heappush(heap, -par)

print(*ans)
