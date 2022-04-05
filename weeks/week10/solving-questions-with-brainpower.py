class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def solveOrSkip(idx):
            if idx >= len(questions):
                return 0
            solve = questions[idx][0] + solveOrSkip(idx + questions[idx][1] + 1) 
            skip = solveOrSkip(idx + 1)
            return max(solve,skip)
        return solveOrSkip(0)
