from collections import defaultdict, deque


def main():

    n, m, s = map(int, input().split())

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    visited = set()

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        in_degree[b] += 1

    def bfs(node):
        visited.add(node)
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neigh in graph[curr]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)

    bfs(s)
    ans = 0

    for i in range(1, n + 1):
        if i in visited:
            continue

        if in_degree[i] == 0:
            bfs(i)
            ans += 1

    nodes = [i for i in range(1, n + 1)]
    nodes.sort(key=lambda x: in_degree[x], reverse=True)

    for node in nodes:
        if i not in visited:
            bfs(i)
            ans += 1

    print(ans)


main()
