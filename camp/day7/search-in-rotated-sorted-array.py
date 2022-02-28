class Solution:
    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        end = right

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left] and nums[mid] < nums[right]:  # mid is still in the second half
                right = mid
                end = right
            # mid is still in the first half
            elif nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid
            else:
                break

        fh = self.binary_search(nums, 0, end-1, target)
        sh = self.binary_search(nums, end, len(nums)-1, target)
        ans = fh
        ans = sh if sh != -1 else ans
        return ans
