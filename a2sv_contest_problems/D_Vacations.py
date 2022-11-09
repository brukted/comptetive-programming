from functools import lru_cache
from sys import stdin, stdout

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))


@lru_cache(None)
def minRest(i=0, last=0):
    # 0 rest, 1 contest, 2 gym
    if i >= len(arr):
        return 0

    if arr[i] == 0:
        return 1 + minRest(i + 1, 0)

    rest = 1 + minRest(i + 1, 0)
    gym = minRest(i + 1, 2)
    contest = minRest(i + 1, 1)

    if arr[i] == 1:  # contest
        if last != 1:
            return min(rest, contest)
        else:
            return rest
    elif arr[i] == 2:  # gym
        if last != 2:
            return min(gym, rest)
        else:
            return rest

    elif arr[i] == 3:  # gym and contest
        if last == 0:  # rest
            return min(rest, min(gym, contest))
        elif last == 1:  # contest
            return min(rest, gym)
        else:  # last is gym
            return min(rest, contest)


print(minRest())
