from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        l = len(nums)
        while j < l:
            n = nums[j]
            while j < l and n == nums[j]:
                j += 1
            nums[i] = n
            i += 1
        return i
