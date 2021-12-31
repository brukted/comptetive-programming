# https://leetcode.com/problems/powx-n/

class Solution:
    def recPos(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if (n % 2) == 1:
            h = self.recPos(x, n//2)
            return x * h * h
        else:
            h = self.recPos(x, n//2)
            return h * h

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.recPos(x, n)
        else:
            return self.recPos(1/x, -n)
