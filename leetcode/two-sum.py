class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_count = {}
        pairs = None
        for idx , num in enumerate(nums):
            if target - num in nums_count:
                pairs = [nums_count[target-num],idx]
                break
            nums_count[num] = idx
        return pairs