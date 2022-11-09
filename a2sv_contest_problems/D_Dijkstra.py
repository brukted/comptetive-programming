from collections import defaultdict, deque
import heapq

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b - 1, w))
    graph[b-1].append((a - 1, w))

prev = [None] * n
disA = [float("inf")] * n
disA[0] = 0

que = [(0, 0)]

while que:
    dis, node, = heapq.heappop(que)

    if node == n - 1:
        break

    for (nei, w) in graph[node]:
        if dis + w < disA[nei]:
            prev[nei] = node
            disA[nei] = dis + w
            heapq.heappush(que, (dis + w, nei))

if prev[-1] == None:
    print("-1")
    exit()

path = []
pr = n - 1

while pr is not None:
    path.append(pr + 1)
    pr = prev[pr]

path.reverse()
print(' '.join(map(str, path)))
