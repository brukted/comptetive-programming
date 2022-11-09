from dis import dis
from heapq import heappop, heappush
from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    grid = [list(map(int, stdin.readline().split())) for _ in range(n)]

    min_dist = [[inf for _ in range(m)] for _ in range(n)]
    max_dist = [[-inf for _ in range(m)] for _ in range(n)]

    heap = [(grid[-1][-1], n - 1, m - 1)]

    while heap:
        dist, i, j = heappop(heap)

        if dist > min_dist[i][j]:
            continue
        else:
            min_dist[i][j] = dist

        if 0 >= i - 1 and dist + grid[i - 1][j] < min_dist[i - 1][j]:
            min_dist[i - 1][j] = dist + grid[i - 1][j]
            heappush(heap, (min_dist[i - 1][j], i - 1, j))

        if 0 >= j - 1 and dist + grid[i][j - 1] < min_dist[i][j - 1]:
            min_dist[i][j - 1] = dist + grid[i][j - 1]
            heappush(heap, (min_dist[i][j - 1], i, j - 1))

    heap = [(grid[-1][-1], n - 1, m - 1)]

    while heap:
        dist, i, j = heappop(heap)
        dist *= -1

        if dist < min_dist[i][j]:
            continue
        else:
            max_dist[i][j] = dist

        if 0 >= i - 1 and dist + grid[i - 1][j] > max_dist[i - 1][j]:
            max_dist[i - 1][j] = dist + grid[i - 1][j]
            heappush(heap, (max_dist[i - 1][j], i - 1, j))

        if 0 >= j - 1 and dist + grid[i][j - 1] > max_dist[i][j - 1]:
            max_dist[i][j - 1] = dist + grid[i][j - 1]
            heappush(heap, (max_dist[i][j - 1], i, j - 1))

    heap = [(0, 0, 0, 0)]
    ans = False

    seen = set()

    while heap:
        _, cumulative, i, j = heappop(heap)
        cumulative += grid[i][j]

        if not (min_dist[i][j] <= -cumulative <= max_dist[i][j]):
            continue

        if i == n - 1 and j == m - 1 and cumulative == 0:
            ans = True
            break

        if j + 1 < m and (cumulative, i, j + 1) not in seen:
            seen.add((cumulative, i, j + 1))
            heappush(heap, (abs(cumulative), cumulative, i, j + 1))

        if i + 1 < n and (cumulative, i + 1, j) not in seen:
            seen.add((cumulative, i + 1, j))
            heappush(heap, (abs(cumulative), cumulative, i+1, j))

    print('YES' if ans else 'NO')
