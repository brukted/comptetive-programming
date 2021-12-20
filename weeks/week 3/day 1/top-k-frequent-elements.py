# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        r = []
        for i in range(k):
            r.append(count[i][0])
        return r
