class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        
        i = 0
        j = 0
        maxx = 0
                
        while j < len(nums):
            if nums[j] == 1:
                j += 1
                maxx = max(maxx, j - i)
            else:
                zeros += 1
                if zeros > k:
                    while nums[i] != 0:
                        i += 1
                    i += 1
                    zeros -= 1
                j += 1
                    
        maxx = max(maxx, j - i)
        
        return maxx
