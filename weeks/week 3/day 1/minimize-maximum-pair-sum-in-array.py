# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        s = nums[0] + nums[-1]
        while i < j:
            s = max(s, nums[i]+nums[j])
            i += 1
            j -= 1
        return s
