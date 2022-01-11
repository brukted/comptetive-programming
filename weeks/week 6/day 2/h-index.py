# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if citations[0] == 0:
            return 0
        for i in range(len(citations)):
            if i == len(citations)-1:
                return i+1
            if citations[i+1] <= i+1:
                return i+1
