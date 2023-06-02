class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:        
        @lru_cache(None)
        def combinationRec(i, t):
            if i  == len(nums):
                return 0
            
            if nums[i] == t:
                return 1 + combinationRec(i + 1 , t)
            elif nums[i] < t:
                return combinationRec(0 , t - nums[i]) + combinationRec(i + 1 , t)
            else:
                return combinationRec(i + 1 , t)
        
        return combinationRec(0, target)
            
        
                