class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        ss = sum(nums)

        @lru_cache(None)
        def solve(target, rem=0, i=0):
            if target == 0 and rem == 0:
                return True

            if i == len(nums) or target < 0 or rem == 0:
                return False

            return solve(target, rem, i + 1) or solve(target - nums[i], rem - 1, i + 1)

        for i in range(1, len(nums)):
            if (ss * i) % len(nums) == 0 and solve((ss * i) // len(nums), i):
                return True

        return False
