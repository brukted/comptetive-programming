class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prev_min= inf
        answer = -inf

        for num in nums:
            if prev_min < num:
                answer = max(answer, num - prev_min)
            prev_min = min(prev_min, num)
        
        return answer if answer != -inf else -1
