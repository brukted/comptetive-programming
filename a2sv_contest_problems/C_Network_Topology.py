from collections import defaultdict, deque
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

degrees = defaultdict(int)
visited = {1}
queue = deque([(1, -1)])

while queue:
    node, parent = queue.popleft()
    degrees[len(graph[node])] += 1

    for nei in graph[node]:
        if nei == parent:
            continue

        if nei not in visited:
            queue.append((nei, node))
            visited.add(nei)

degrees = list(degrees.items())
degrees.sort()

if len(visited) != n:
    print("unknown topology")
elif n >= 4 and len(degrees) == 2 and degrees[0] == (1, n - 1) and degrees[1] == (n - 1, 1):
    print("star topology")
elif n > 2 and len(degrees) == 1 and degrees[0][0] == 2:
    print("ring topology")
elif n == 2 and len(degrees) == 1 and degrees[0][0] == 2:
    print("ring topology")
elif ((len(degrees) == 1 and n <= 2) or (len(degrees) == 2 and degrees[0] == (1, 2) and degrees[1] == (2, n - 2))):
    print("bus topology")
else:
    print("unknown topology")
