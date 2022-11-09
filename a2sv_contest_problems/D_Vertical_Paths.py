from collections import defaultdict, deque
from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    tree = defaultdict(list)
    arr = list(map(int, stdin.readline().split()))
    root = None

    out_degree = [0] * (n + 1)

    for i in range(n):
        if arr[i] != i + 1:
            tree[arr[i]].append(i + 1)
            out_degree[arr[i]] += 1
        else:
            root = i + 1

    # topsort, leaves to root
    max_path = [0] * (n + 1)

    start = filter(lambda i: out_degree[i] == 0, range(1, n + 1))
    queue = deque(map(lambda i: (i, 0), start))

    while queue:
        node, depth = queue.popleft()
        max_path[node] = depth

        if node == root:
            continue

        out_degree[arr[node - 1]] -= 1
        if out_degree[arr[node - 1]] == 0:
            queue.append((arr[node - 1], depth + 1))

    ans = [[]]

    queue = deque([(root, ans[-1])])

    while queue:
        node, path = queue.popleft()
        path.append(node)

        if len(tree[node]) == 0:
            continue

        max_node = None
        maxx = -inf
        for child in tree[node]:
            if max_path[child] > maxx:
                maxx = max_path[child]
                max_node = child

        queue.append((max_node, path))

        for child in tree[node]:
            if child != max_node:
                ans.append([])
                queue.append((child, ans[-1]))

    print(len(ans))
    for path in ans:
        print(len(path))
        print(*path)
    print()
