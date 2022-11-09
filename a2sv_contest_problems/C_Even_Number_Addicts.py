from functools import lru_cache
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    count = [0, 0]
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    for num in arr:
        count[num % 2] += 1

    @lru_cache(None)
    def canAliceWin(isAlice=True, evens=count[0], odds=count[1], a_mod=0, b_mod=0):
        if evens + odds == 0:
            return a_mod == 0

        if isAlice:
            can_win = False
            if evens > 0:
                can_win |= canAliceWin(not isAlice, evens - 1, odds, a_mod, b_mod)
            
            if odds > 0:
                can_win |= canAliceWin(not isAlice, evens, odds - 1, (a_mod + 1) % 2, b_mod)
            
            return can_win
        else:
            can_win = True
            if evens > 0:
                can_win &= canAliceWin(not isAlice, evens - 1, odds, a_mod, b_mod)

            if odds > 0:
                can_win &= canAliceWin(not isAlice, evens, odds - 1, a_mod, (b_mod + 1) % 2)
            
            return can_win

    print('Alice' if canAliceWin() else 'Bob')
    canAliceWin.cache_clear()
