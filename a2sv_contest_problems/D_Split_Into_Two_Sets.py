from collections import defaultdict, deque
from sys import stdin


def isBipartite(node, colors, graph):
    colors[node] = 0

    queue = deque([node])
    while queue:
        n = queue.popleft()

        for nei in graph[n]:
            if colors[nei] == -1:
                colors[nei] = 1 - colors[n]
                queue.append(nei)
            elif colors[nei] == colors[n]:
                return False

    return True


def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        n = int(stdin.readline())
        graph = defaultdict(list)

        can = True

        for i in range(n):
            u, v = map(int, stdin.readline().split())

            if can:
                graph[u].append(v)
                graph[v].append(u)

                if u == v:
                    can = False
                if len(graph[i]) > 2:
                    can = False
        
        if not can:
            print('NO')
            continue

        colors = defaultdict(lambda: -1)

        for i in graph.keys():
            if colors[i] == -1:
                if not isBipartite(i, colors, graph):
                    can = False
                    break

        print('YES' if can else 'NO')


main()
