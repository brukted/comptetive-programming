from functools import lru_cache
from sys import stdin, stdout


def findL(m, s, isFirst=True):
    if m == 0:
        return -1 if s != 0 else ""

    if s == m:
        return "1" * s

    for i in range(9, 0 if isFirst else -1, -1):
        ans = findL(m - 1, s - i, False)
        if ans != -1:
            return str(i) + ans

    return -1


def findS(m, s, isFirst=True):
    if m == 0:
        return -1 if s != 0 else ""

    if s < 0:
        return -1

    for i in range(1 if isFirst else 0, 10):
        ans = findS(m - 1, s - i, False)
        if ans != -1:
            return str(i) + ans

    return -1


m, s = map(int, stdin.readline().split())
if s == 0 and m == 1:
    print(0, 0)
else:
    print(int(findS(m, s)), int(findL(m, s)))
