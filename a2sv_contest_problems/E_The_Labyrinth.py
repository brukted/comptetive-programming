from itertools import product
from sys import stdin, stdout


class UnionFind:
    def __init__(self, items) -> None:
        self.parent = {item: item for item in items}
        self.size = {item: 1 for item in items}

    def find(self, k):
        stack = [k]
        while self.parent[stack[-1]] != stack[-1]:
            stack.append(self.parent[stack[-1]])
        root = stack.pop()
        while stack:
            self.parent[stack.pop()] = root
        return root

    def union(self, a, b):
        a_p = self.find(a)
        a_s = self.size[a_p]

        b_p = self.find(b)
        b_s = self.size[b_p]

        if a_p == b_p:
            return

        if a_s < b_s:
            b_p, b_s, a_p, a_s = a_p, a_s, b_p, b_s

        self.parent[b_p] = a_p
        self.size[a_p] += b_s


n, m = map(int, stdin.readline().split())

grid = [list(stdin.readline()) for _ in range(n)]

dsu = UnionFind(list(((i, j) for i in range(n) for j in range(m))))
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def inbound(i, j):
    return 0 <= i < n and 0 <= j < m


for (i, j) in product(range(n), range(m)):
    if grid[i][j] == '*':
        continue

    for (di, dj) in [(1, 0), (0, 1)]:
        ni, nj = i + di, j + dj

        if inbound(ni, nj) and grid[ni][nj] == '.':
            dsu.union((i, j), (ni, nj))

for i in range(n):
    for j in range(m):

        if grid[i][j] == '.':
            stdout.write('.')
            continue
        else:
            visited = set()
            ans = 1

            for (di, dj) in dirs:
                ni, nj = i + di, j + dj

                if inbound(ni, nj) and grid[ni][nj] == '.' and dsu.find((ni, nj)) not in visited:
                    ans += dsu.size[dsu.find((ni, nj))]
                    visited.add(dsu.find((ni, nj)))

            stdout.write(str(ans % 10))

    stdout.write("\n")
