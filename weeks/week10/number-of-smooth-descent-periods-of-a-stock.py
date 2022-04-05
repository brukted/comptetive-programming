class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        i = 0
        j = 1
        total = 0
        while j < len(prices):
            if prices[j-1] == prices[j] + 1:
                j += 1
            else:
                for k in range(j - i):
                    total += j - i - k 
                i = j
                j += 1
        for k in range(j - i):
            total += j - i - k 
        return total
            
