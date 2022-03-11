class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {len(nums) - 1 : nums[-1]}
        
        def robRec(house):
            house_stash = nums[house]
            sub_rob = 0
            
            for next_house in range(house+2,len(nums)):
                sub_rob = max(sub_rob , memo[next_house] if next_house in memo else robRec(next_house))
            memo[house] = house_stash + sub_rob
            return memo[house]
        
        for house in range(len(nums)):
            if house not in memo:
                robRec(house)
        
        return max(memo.values())