from sys import stdin, stdout


def main():
    s = stdin.readline().strip()
    s = s[::-1]
    MOD = (10 ** 9) + 7

    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    dp[-1] = 1

    if s[0] == 'w' or s[0] == 'm':
        print(0)
        exit()

    for i in range(1, len(s)):
        if s[i] == 'w' or s[i] == 'm':
            print(0)
            exit()

        if s[i] == 'u' or s[i] == 'n':
            if s[i - 1] == s[i]:
                dp[i] = (dp[i - 2] + dp[i - 1]) % MOD
            else:
                dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]

    print(dp[-1])


main()
