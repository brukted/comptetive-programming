class Solution:
    def findRight(self, nums, target):
        best = -1
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                best = mid
                left = mid + 1
        return best

    def findLeft(self, nums, target):
        best = -1
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                best = mid
                right = mid - 1
        return best

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findLeft(nums, target), self.findRight(nums, target)]
