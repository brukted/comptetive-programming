# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [None] * len(nums)
        i = 0
        front = 0
        last = -1
        while front != len(nums)+last:
            if i % 2 == 0:
                result[i] = nums[last]
                last -= 1
            else:
                result[i] = nums[front]
                front += 1
            i += 1
        result[-1] = nums[last]
        return result
