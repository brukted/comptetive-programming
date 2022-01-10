# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        j = 1
        l = []
        while j <= n:
            l.append(j)
            j += 1
        # Current item
        i = 0
        while len(l) > 1:
            i += k-1
            i %= len(l)
            l.pop(i)
        return l[-1]
