from sys import stdin
import sys
import threading


def main():
    n = int(stdin.readline().strip())

    s = stdin.readline().strip()
    arr = list(map(int, stdin.readline().split()))

    hard = "hard"

    dp = [[None for _ in range(n)] for _ in range(4)]

    def ans(i, j):
        if j == n:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        cur_amb = arr[j]
        if i == 3 and hard[i] == s[j]:
            dp[i][j] = arr[j]
        elif hard[i] == s[j]:
            dp[i][j] = min(cur_amb + ans(i, j + 1), ans(i + 1, j + 1))
        else:
            dp[i][j] = ans(i, j + 1)

        return dp[i][j]

    print(ans(0, 0))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()