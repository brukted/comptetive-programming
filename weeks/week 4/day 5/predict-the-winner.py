# https://leetcode.com/problems/predict-the-winner/
from typing import List


class Solution:
    def score(self, nums: List[int], player1: bool, score, i, j):
        if j == i:
            if player1:
                return [score[0]+nums[i], score[1]]
            else:
                return [score[0], score[1]+nums[i]]

        if player1:
            pA = self.score(nums, not player1, [
                            score[0] + nums[i], score[1]], i+1, j)
            pB = self.score(nums, not player1, [
                            score[0] + nums[j], score[1]], i, j-1)
            if pA[0] > pB[0]:
                return pA
            else:
                return pB
        else:
            pA = self.score(nums, not player1, [
                            score[0], score[1] + nums[i]], i+1, j)
            pB = self.score(nums, not player1, [
                            score[0], score[1] + nums[j]], i, j-1)
            if pA[0] < pB[0]:
                return pA
            else:
                return pB

    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.score(nums, True, [0, 0], 0, len(nums)-1)
        if score[0] >= score[1]:
            return True
        else:
            return False
