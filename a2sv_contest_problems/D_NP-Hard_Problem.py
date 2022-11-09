from collections import defaultdict, deque
from sys import stdin, stdout


def bipartite(graph, s, colors):
    colors[s] = 0

    queue = deque([s])
    while queue:
        n = queue.popleft()

        for nei in graph[n]:
            if colors[nei] == -1:
                colors[nei] = 1 - colors[n]
                queue.append(nei)
            elif colors[nei] == colors[n]:
                return -1


n, m = map(int, stdin.readline().split())

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

colors = defaultdict(lambda: -1)
for i in range(1, n + 1):
    if i not in colors and len(graph[i]) != 0:
        if bipartite(graph, i, colors) == -1:
            print(-1)
            exit()

groups = {0: [], 1: []}

for node in colors.keys():
    groups[colors[node]].append(node)

print(len(groups[1]))
print(*groups[1])
print(len(groups[0]))
print(*groups[0])
