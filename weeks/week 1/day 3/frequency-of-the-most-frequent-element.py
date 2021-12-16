# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        gMax = 0
        i = 0
        j = 0
        l = len(nums)
        while j < l:
            if (nums[i] - nums[j]) <= k:
                k -= nums[i] - nums[j]
                j += 1
            else:
                currMax = j - i
                k += (nums[i] - nums[i+1]) * (currMax-1)
                gMax = max(gMax, currMax)
                i += 1
        gMax = max(gMax, j-i)
        return gMax
