# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            subArray = nums[l[i]:r[i]+1]
            subArray.sort()
            d = subArray[1]-subArray[0]
            for j in range(len(subArray)-1):
                if d != subArray[j+1]-subArray[j]:
                    result.append(False)
                    break
            if len(result) != i+1:
                result.append(True)
        return result
