from collections import deque
from itertools import product
from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())

grid = [list(input()) for _ in range(n)]

si, sj, count = 0, 0, 0
for (i, j) in product(range(n), range(m)):
    if grid[i][j] == '.':
        count += 1
        si, sj = i, j

queue = deque([(si, sj)])
visited = {(si, sj)}

while queue:
    i, j = queue.popleft()
    count -= 1
    if count < k:
        grid[i][j] = 'X'

    for (di, dj) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '.' and (ni, nj) not in visited:
            visited.add((ni, nj))
            queue.append((ni, nj))

print(*map(lambda row: ''.join(row), grid), sep='\n')
