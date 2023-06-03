class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def ways(i = 0, t = target):
            if i == len(nums):
                if 0 == t: return 1
                else: return 0
            return ways(i + 1, t + nums[i]) + ways(i + 1, t - nums[i])
            
        return ways()