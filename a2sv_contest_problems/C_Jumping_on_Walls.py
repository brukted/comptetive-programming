from collections import deque


def main():
    n, k = map(int, input().split())
    wall = [input(), input()]

    queue = deque([(0, 0, 0)])
    visited = set()

    while queue:
        i, j, depth = queue.popleft()

        if (i, j) in visited:
            continue

        visited.add((i, j))

        if j + k >= n:
            print('YES')
            exit()

        if wall[i][j + 1] == '-' and (i, j + 1) not in visited:
            queue.append((i, j + 1, depth + 1))

        if j - 1 > depth and j - 1 > -1 and wall[i][j - 1] == '-' and (i, j - 1) not in visited:
            queue.append((i, j - 1, depth + 1))

        if wall[(i + 1) % 2][j + k] == '-' and ((i + 1 % 2, j + k)) not in visited:
            queue.append(((i + 1) % 2, j + k, depth + 1))

    print("NO")


main()
