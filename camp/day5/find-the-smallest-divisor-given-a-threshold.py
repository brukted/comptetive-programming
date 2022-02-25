class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1  # Resuts in the maximum result
        right = max(nums)  # Causes the res to be 1
        best = 1

        while left <= right:
            mid = (left+right) // 2
            val = 0
            for i in nums:
                val += int(ceil(i/mid))
            if val > threshold:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return best
