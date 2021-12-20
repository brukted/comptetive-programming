# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles) - 1
        s = 0
        while i < j-1:
            s += piles[j-1]
            i += 1
            j -= 2
        return s
