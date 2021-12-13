from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numss = []
        for n in nums:
            numss.append(int(n))
        numss.sort(reverse=True)
        return str(numss[k-1])
