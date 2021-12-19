# https://leetcode.com/problems/find-original-array-from-doubled-array/
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        i = 0
        j = i+1
        result = []
        chLen = len(changed)
        while j < chLen:
            if changed[j] == changed[i] * 2:
                result.append(changed[i])
                changed[j] = -1
                changed[i] = -1
                while i < chLen and changed[i] == -1:
                    i += 1
                j = max(i+1, j)
            else:
                j += 1
        if len(result) * 1.0 != chLen / 2:
            return []
        return result
