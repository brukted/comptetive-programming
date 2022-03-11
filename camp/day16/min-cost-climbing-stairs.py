class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        
        def gotoX(x):
            if x + 1 == len(cost) or x + 2 == len(cost):
                memo[x] = cost[x]
            else:
                jump_1 = memo[x+1] if x + 1 in memo else gotoX(x + 1)
                jump_2 = memo[x+2] if x + 2 in memo else gotoX(x + 2)
                memo[x] = min(jump_1,jump_2) + cost[x]
            return memo[x]
        gotoX(0)
        if not 1 in memo:
            gotoX(1)
        
        return min(memo[0],memo[1])