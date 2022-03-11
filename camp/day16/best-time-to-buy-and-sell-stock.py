class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = prices[-1]
        
        for day in range(len(prices) - 2, -1 ,-1):
            max_price = max(prices[day], max_price)
            max_profit = max(max_profit, max_price- prices[day])
            
        return max_profit