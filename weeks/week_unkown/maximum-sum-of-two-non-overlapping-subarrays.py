class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        len1_sum = sum(nums[:firstLen])
        max_len1 = len1_sum
        len2_sum = sum(nums[firstLen:firstLen + secondLen])
        
        maxx = len1_sum + len2_sum
        
        for i in range(firstLen, len(nums) - secondLen):
            len1_sum += nums[i] - nums[i - firstLen]
            max_len1= max(max_len1, len1_sum)
            
            len2_sum += nums[i + secondLen] - nums[i]
            
            maxx = max(maxx, max_len1+ len2_sum)
        
        maxx = max(maxx, max_len1+ len2_sum)
        
        len2_sum = sum(nums[:secondLen])
        len1_sum = sum(nums[secondLen:firstLen + secondLen])
        max_len2 = len2_sum
        
        maxx = max(maxx, len1_sum + len2_sum)
        
        for i in range(secondLen, len(nums) - firstLen):            
            len2_sum += nums[i] - nums[i - secondLen]
            max_len2 = max(max_len2, len2_sum)
            
            len1_sum += nums[i + firstLen] - nums[i]

            maxx = max(maxx, max_len2+ len1_sum)
        
        maxx = max(maxx, max_len2+ len1_sum)
        return maxx
