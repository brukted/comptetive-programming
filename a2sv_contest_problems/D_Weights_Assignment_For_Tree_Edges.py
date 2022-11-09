from collections import defaultdict, deque
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    b = list(map(int, stdin.readline().split()))
    p = list(map(int, stdin.readline().split()))

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    root = -1

    for idx, b_i in enumerate(b):
        if idx + 1 == b_i:
            root = b_i
            continue

        graph[b_i].add(idx + 1)
        in_degree[idx + 1] += 1
    
    for idx, p_i in enumerate(p[:-1]):
        if p[idx + 1] not in graph[p_i]:
            graph[p_i].add(p[idx + 1])
            in_degree[p[idx + 1]] += 1

        if in_degree[root] >= 1:
            break
    
    if in_degree[root] >= 1:
        print(-1)
        continue

    distance = 0
    distances = [None] * n
    distances[root - 1] = 0
    
    weights = [None] * n
    weights[root - 1] = 0

    processed = 0

    que = deque([root])


    while que:
        node = que.popleft()
        distances[node - 1]= distance
        distance += 1

        weights[node - 1] = distances[node - 1] - distances[b[node - 1] - 1]
        processed += 1

        for nei in graph[node]:
            in_degree[nei] -= 1

            if in_degree[nei] == 0:
                que.append(nei)

    if processed != n:
        print(-1)
    else:
        print(*weights)
