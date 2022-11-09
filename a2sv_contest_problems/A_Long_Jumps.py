from sys import stdin


def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))

        dp = [0] * n
        dp[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            dp[i] = arr[i]

            if i + arr[i] < n:
                dp[i] += dp[i + arr[i]]

        ans = 0

        # print(dp)
        for i in range(n):
            ans = max(arr[i], ans)  # curr only

            if i + arr[i] < n:
                ans = max(arr[i] + dp[i + arr[i]], ans)

        print(ans)

main()