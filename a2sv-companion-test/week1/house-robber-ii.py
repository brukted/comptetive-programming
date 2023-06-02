class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def robRec(house, firstRobbed):
            if house >= len(nums):
                return 0
            
            if house == len(nums) - 1:
                if firstRobbed:
                    return 0
                else:
                    return nums[house]
            
            return max(robRec(house + 1, firstRobbed), nums[house] + robRec(house + 2, firstRobbed))
        
        return max(robRec(1, False), nums[0] + robRec(2, True))