from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = []

    for _ in range(n):
        grid.append(list(input()))

    stones = []

    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j] == '*':
                stones.append((i, j))

    queue = deque(stones, maxlen=len(stones))

    while queue:
        i, j = queue.popleft()

        if i == n - 1:
            continue

        if grid[i + 1][j] == '.':
            grid[i + 1][j] = '*'
            grid[i][j] = '.'
            queue.append((i + 1, j))

    for i in range(n):
        for j in range(m):
            print(grid[i][j],sep='',end='')
        print()

    # print()
