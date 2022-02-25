"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        solutions = []
        for x in range(1, 1001):
            left = 1
            right = 1000
            while left <= right:  # breaks when the solution is found
                mid = (left + right) // 2
                val = customfunction.f(x, mid)
                if val < z:
                    left = mid + 1
                elif val > z:
                    right = mid - 1
                else:
                    solutions.append([x, mid])
                    break
        return solutions
