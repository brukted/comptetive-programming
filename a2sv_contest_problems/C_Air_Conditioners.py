from math import inf
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    input()

    n, k = map(int, stdin.readline().split())
    a = list(map(lambda x: int(x) - 1, stdin.readline().split()))
    t = list(map(int, stdin.readline().split()))

    at = list(zip(a, t))
    at.sort()
    cells = [inf] * n

    # left to right
    l_idx = 0
    left = inf

    for i in range(n):
        while l_idx < k and at[l_idx][0] <= i:
            left = min(left, at[l_idx][1] + i - at[l_idx][0])

            if left == inf:
                left = 0

            l_idx += 1

        cells[i] = left
        left += 1

    # right to left
    r_idx = k - 1
    right = inf

    for i in range(n - 1, -1, -1):

        while r_idx > -1 and at[r_idx][0] >= i:
            right = min(right, at[r_idx][1] + at[r_idx][0] - i)

            if right == inf:
                right = 0

            r_idx -= 1

        cells[i] = min(cells[i], right)
        right += 1

    for i in range(n):
        if cells[i] == inf:
            cells[i] = 0

    print(*cells)
