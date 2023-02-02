class Solution:
    def numberOfWays(self, s: str) -> int:
        answer = 0
        left_zeros = left_ones = 0
        one_zeros = zero_ones = 0

        for _, num in enumerate(map(int, s)):
            # 0 1 0
            if num == 0:
                answer += zero_ones
                left_zeros += 1
                one_zeros += left_ones
            # 1 0 1
            else:
                answer += one_zeros
                left_ones += 1
                zero_ones += left_zeros

        return answer
