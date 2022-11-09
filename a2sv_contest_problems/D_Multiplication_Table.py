from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())


def search(n=n, m=m):
    l = 1
    r = n * m
    best = 0

    while l <= r:
        mid = (l + r) // 2

        less = 0

        for i in range(1, n + 1):
            less += min(m, mid // i)

        if less >= k:
            best = mid
            r = mid - 1
        else:
            l = mid + 1

    return best


print(search())
