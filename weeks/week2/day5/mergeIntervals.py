# https://leetcode.com/problems/merge-intervals/submissions/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1] = [result[-1][0],
                              max(intervals[i][1], result[-1][1])]

        return result
