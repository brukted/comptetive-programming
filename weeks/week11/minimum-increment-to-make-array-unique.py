class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                moves += nums[i-1] - nums[i] + 1
                nums[i] += nums[i-1] - nums[i] + 1
        return moves
