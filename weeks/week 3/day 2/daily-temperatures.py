# https://leetcode.com/problems/daily-temperatures/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mono = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            # There are no days before
            if len(mono) == 0:
                mono.append(i)
                continue

            # Warmer day encountered
            if temperatures[mono[-1]] < temp:
                # While there are days and colder days before this
                while len(mono) > 0 and temperatures[mono[-1]] < temp:
                    result[mono[-1]] = i - mono[-1]
                    mono.pop()
                mono.append(i)
            # Colder day enountered
            else:
                mono.append(i)

        return result
