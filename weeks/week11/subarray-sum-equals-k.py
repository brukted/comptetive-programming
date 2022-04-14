class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefix_count = defaultdict(lambda : 0)
        prefix_count[0] = 1
        sub_arrays = 0
        
        for num in nums:
            prefix += num
            sub_arrays += prefix_count[prefix - k]
            prefix_count[prefix] += 1
        
        return sub_arrays
