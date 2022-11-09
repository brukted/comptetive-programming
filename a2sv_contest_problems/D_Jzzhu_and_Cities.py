from heapq import heappop, heappush
from collections import defaultdict
from math import inf
from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
graph = defaultdict(list)

trains = {}
multiples = 0

for _ in range(m):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w, 0))
    graph[v].append((u, w, 0))


for _ in range(k):
    s, y = map(int, stdin.readline().split())
    if s in trains:
        trains[s] = min(trains[s], y)
        multiples += 1
    else:
        trains[s] = y

for (dest, dis) in trains.items():
    graph[1].append((dest, dis, 1))


def dijkstra(graph):
    dist = defaultdict(lambda: inf)
    visited = set()
    dist[1] = 0

    queue = [(0, 1, 0)]
    skippables = 0

    while queue:
        path_len, node, train = heappop(queue)

        if node not in visited:
            visited.add(node)

            for nei, edge_len, is_train in graph[node]:
                if edge_len + path_len <= dist[nei] or is_train:
                    dist[nei] = edge_len + path_len
                    heappush(queue, (edge_len + path_len, nei, is_train))

        elif train == 1:
            skippables += 1

    return skippables


print((multiples + dijkstra(graph)))
