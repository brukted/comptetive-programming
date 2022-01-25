from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        best = 0
        while left != right:
            best = max(best,(right-left) * min(height[left],height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best