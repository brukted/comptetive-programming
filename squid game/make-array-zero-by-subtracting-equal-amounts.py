class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        answer = prefix = 0
        for num in nums:
            num -= prefix
            if num == 0:
                continue
            else:
                answer += 1
                prefix += num
        return answer
