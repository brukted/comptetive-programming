t = int(input())

for _ in range(t):
    n = int(input())
    moves = 0

    grid = []
    for _ in range(n):
        grid.append(input())

    seen = set()

    for i in range(n // 2):
        ul = (i,  i)
        ll = (n - 1 - i, i)
        ur = (i,  n - 1 - i)
        lr = (n - 1 - i, n - 1 - i)

        while ul not in seen:
            # print(ul, ur)
            # print(ll, lr)
            c = int(grid[ul[0]][ul[1]]) + int(grid[ll[0]][ll[1]]) + \
                int(grid[ur[0]][ur[1]]) + int(grid[lr[0]][lr[1]])

            moves += min(4 - c, c)

            seen.add(ul)
            seen.add(ll)
            seen.add(ur)
            seen.add(lr)
            ul = ul[0] +1, ul[1]
            ur = ur[0]    , ur[1] - 1
            ll = ll[0]    , ll[1] + 1
            lr = lr[0] - 1, lr[1]
    print(moves)
