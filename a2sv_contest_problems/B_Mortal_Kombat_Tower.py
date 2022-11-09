from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))
    i = 0
    is_easy = False
    skips = 0

    dp = [[None for _ in range(n + 1)] for _ in range(2)]

    dp[0][-2] = arr[-1]
    dp[1][-2] = 0

    dp[0][-1] = 0
    dp[1][-1] = 0

    for i in range(n - 2, -1, -1):
        dp[0][i] = min(arr[i] + arr[i+1] + dp[1][i + 2], arr[i] + dp[1][i+1])
        dp[1][i] = min(0 + dp[0][i + 2], dp[0][i+1])

    # print(dp)
    print(dp[0][0])
