# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for i in nums:
            count[i] += 1

        num_less = 0
        for i in range(len(count)):
            temp = count[i]
            count[i] = num_less
            num_less += temp
        result = []
        for i in nums:
            result += [count[i]]
        return result
