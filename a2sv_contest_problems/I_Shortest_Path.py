from collections import defaultdict, deque
from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())

graph = defaultdict(list)

tr = defaultdict(lambda: defaultdict(set))

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in range(k):
    a, b, c = map(int, stdin.readline().split())
    tr[b][a].add(c)

queue = deque([(-1, 1, 0)])
prevs = {(-1, 1): -1}
visited = {(1, -1)}

while queue:
    prev, node, depth = queue.popleft()
    ttt = tr[node][prev]

    if node == n:
        path = [node]

        while prev != -1:
            prev, node = prevs[(prev, node)]
            path.append(node)

        path.reverse()
        
        print(depth)
        print(*path)
        exit()

    for nei in graph[node]:
        if (node, nei) not in visited and nei not in ttt:
            visited.add((node, nei))
            prevs[(node, nei)] = (prev, node)
            queue.append((node, nei, depth + 1))


print(-1)
