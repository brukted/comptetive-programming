from functools import lru_cache
n, l, r = map(int, input().split())


@lru_cache(53)
def count(x=n):
    if x == 1 or x == 0:
        return 1
    return count(x // 2) * 2 + 1


l -= 1
r -= 1


def ans(x=n, n_idx=0):
    a = 0

    if x == 1 or x == 0:
        if l <= n_idx <= r:
            return x
        return 0

    if n_idx <= r and n_idx + count(x // 2) >= l:
        a += ans(x//2, n_idx)

    n_idx += count(x // 2)

    if l <= n_idx <= r:
        a += x % 2

    n_idx += 1

    if n_idx <= r and n_idx + count(x // 2) >= l:
        a += ans(x//2, n_idx)

    return a


print(ans())
