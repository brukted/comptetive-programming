# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        dic = {}
        for i in nums:
            if k - i in dic and dic[k-i] > 0:
                dic[k-i] -= 1
                ops += 1
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return ops
