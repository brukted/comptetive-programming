# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        for j in nums:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        k = 0
        for val in dic.values():
            k += comb(val, 2)
        return k
