from collections import defaultdict, deque
from string import ascii_lowercase
from sys import stdin

t = int(stdin.readline().strip())


for _ in range(t):
    s = stdin.readline().strip()

    graph = {ch: set() for ch in ascii_lowercase}

    for idx in range(len(s) - 1):
        graph[s[idx]].add(s[idx + 1])
        graph[s[idx + 1]].add(s[idx])

    in_degree = {ch: len(graph[ch]) for ch in ascii_lowercase}

    if any(map(lambda x: in_degree[x] > 2, ascii_lowercase)):
        print("NO")
        continue

    start = [ch for ch in ascii_lowercase if in_degree[ch] <= 1]
    ss = set(start)

    for ch in ascii_lowercase:
        if ch not in ss:
            start.append(ch)

    ans, seen = [], set()

    solved = True

    for node in start:
        if node in seen:
            continue

        parent = -1
        while node not in seen and node != None:
            seen.add(node)
            ans.append(node)

            next = None

            for nei in graph[node]:
                if nei == parent:
                    continue
                next = nei
            parent = node
            node = next

        if node != None and node in seen:
            solved = False

        if solved == False:
            break
    
    if solved:
        print("YES")
        print("".join(ans))
    else:
        print("NO")
