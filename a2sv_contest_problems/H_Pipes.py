from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    up = list(map(int, list(input())))
    lower = list(map(int,  list(input())))

    dp = [up[0] < 3, up[0] > 2 and lower[0] > 2]

    for i in range(len(up) - 1):
        nxt_dp = [False, False]

        nxt_dp[0] |= dp[0] and up[i + 1] < 3
        nxt_dp[1] |= dp[0] and up[i + 1] > 2 and lower[i + 1] > 2

        nxt_dp[0] |= dp[1] and lower[i + 1] > 2 and up[i + 1] > 2
        nxt_dp[1] |= dp[1] and lower[i + 1] < 3

        dp = nxt_dp

    print("YES" if dp[1] else "NO")
