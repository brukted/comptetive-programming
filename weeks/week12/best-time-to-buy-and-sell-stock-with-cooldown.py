class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def pickDontPick(i,buying):
            if i >= len(prices):
                return 0
            
            if i == len(prices) - 1:
                return 0 if buying else prices[-1]
            
            if buying:
                pick = -prices[i] + pickDontPick(i+1,False)
                dontPick = pickDontPick(i+1,True)
                return max(pick,dontPick)
            else: # Selling
                pick = prices[i] + pickDontPick(i+2,True)
                dontPick = pickDontPick(i+1,False)
                return max(pick,dontPick)
        return pickDontPick(0,True)
