from sys import stdin, stdout
from collections import deque


n, m = map(int, stdin.readline().split())
grid = [list(input()) for _ in range(n)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_inbound(i, j):
    return 0 <= i < n and 0 <= j < m


visited = set()


def check_cycle(start_i, start_j):
    queue = deque([(start_i, start_j, -1, -1)])
    visited.add((start_i, start_j))

    while queue:
        i, j, parent_i, parent_j = queue.popleft()

        for (di, dj) in directions:
            ni, nj = i + di, j + dj
            if (ni, nj) == (parent_i, parent_j):
                continue

            if is_inbound(ni, nj) and grid[ni][nj] == grid[i][j]:
                if (ni, nj) in visited:
                    return True
                queue.append((ni, nj, i, j))
                visited.add((ni, nj))

    return False


for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            if check_cycle(i, j):
                print(("Yes"))
                exit()

print("No")
