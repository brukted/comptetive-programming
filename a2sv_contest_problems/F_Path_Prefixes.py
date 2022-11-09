from collections import defaultdict
from sys import setrecursionlimit, stdin, stdout
import sys
import threading


def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        n = int(stdin.readline().strip())
        tree = defaultdict(list)

        for i in range(1, n):
            p, a, b = map(int, stdin.readline().split())
            tree[p].append((i + 1, a, b))

        ans = [0] * (n + 1)
        bi_sum = [0]

        def solve(a_sum):
            best = 0
            l, r = 0, len(bi_sum) - 1

            while l <= r:
                mid = (l + r) // 2
                val = bi_sum[mid]

                if val <= a_sum:
                    best = mid
                    l = mid + 1
                else:
                    r = mid - 1

            return best

        def dfs(node=1, a=0):
            ans[node] = solve(a)

            for (nei, aj, b) in tree[node]:
                bi_sum.append(bi_sum[-1] + b)
                dfs(nei, a + aj)
                bi_sum.pop()

        dfs()
        print(*ans[2:])


sys.setrecursionlimit(100 + (2 * 10 ** 5))
threading.stack_size(1 << 26)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
