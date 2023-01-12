class Solution:
    def maxJump(self, stones: List[int]) -> int:
        diff_1 = 0
        for i in range(2, len(stones), 2):
            diff_1 = max(diff_1, stones[i] - stones[i - 2])
        
        diff_2 = 0
        for i in range(1, len(stones), 2):
            diff_2 = max(diff_2, stones[i] - stones[max(i - 2, 0)])

        return max(diff_1, diff_2)