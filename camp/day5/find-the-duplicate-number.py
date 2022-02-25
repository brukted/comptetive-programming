class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1  # number of max unique numbers
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2

            nums_larger = 0
            for i in nums:
                if i > mid:
                    nums_larger += 1

            if nums_larger > n - mid:
                left = mid + 1
            else:
                right = mid

        return left
