class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 3, -1, -1):
            if nums[i + 2] - nums[i] < nums[i + 1] < nums[i + 2] + nums[i]:
                return nums[i] + nums[i + 2] + nums[i + 1]

        return 0
