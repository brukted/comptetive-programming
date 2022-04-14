class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix = 0
        right_prefix = sum(nums) - nums[0]
        
        i = 0
        while True:
            if left_prefix == right_prefix:
                return i
            i += 1
            if i >= len(nums):
                break
            left_prefix += nums[i-1]
            right_prefix -= nums[i]
        
        return -1
