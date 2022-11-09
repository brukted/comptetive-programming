from math import inf
from collections import defaultdict, deque
from heapq import heappop, heappush
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    parent = [-1]
    parent.extend(map(lambda x: int(x) - 1, stdin.readline().split()))
    out_degree = [0] * n

    for p in parent[1:]:
        out_degree[p] += 1
    
    leaves = filter(lambda x: out_degree[x] == 0, range(n))
    que = deque(list(map(lambda x: (x, 0), leaves)))

    heap = []

    while que:
        node, depth = que.popleft()
        if node == 0 or parent[node] == 0:
            continue

        heappush(heap, (-depth, node))
        out_degree[parent[node]] -= 1
        if out_degree[parent[node]] == 0:
            que.append((parent[node], depth + 1))

    while heap and k > 0:
        depth, node = heappop(heap)
        depth = -depth

        if parent[node] == 0:
            continue

        parent[node] = 0
        k -= 1

    children = defaultdict(list)

    for idx, p in enumerate(parent):
        children[p].append(idx)

    ans = 1
    que = deque([(0, 0)])
    while que:
        node, depth = que.popleft()
        ans = max(ans, depth)
        for child in children[node]:
            que.append((child, depth + 1))
    
    print(ans)
