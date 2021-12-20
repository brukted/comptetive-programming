# https://leetcode.com/problems/reduce-array-size-to-the-half/
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        s = 0
        lHalf = len(arr)//2
        r = 0
        for i in count:
            s += i[1]
            r += 1
            if s >= lHalf:
                break
        return r
