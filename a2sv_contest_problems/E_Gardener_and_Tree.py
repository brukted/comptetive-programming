from collections import defaultdict, deque
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    stdin.readline().strip()  # Skip line
    n, k = map(int, stdin.readline().split())

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for _ in range(n - 1):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        in_degree[u] += 1
        in_degree[v] += 1

    starting_nodes = list(map(lambda x: (x, 0), filter(
        lambda x: in_degree[x] <= 1, range(1, n + 1))))

    deleted = 0
    starting_nodes = deque(starting_nodes)
    
    while starting_nodes:
        node, depth = starting_nodes.popleft()
        deleted += 1

        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 1 and depth + 1 < k:
                starting_nodes.append((nei, depth + 1))
    
    print(n - deleted)
