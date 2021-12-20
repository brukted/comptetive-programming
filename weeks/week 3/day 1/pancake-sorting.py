# https://leetcode.com/problems/pancake-sorting/
from typing import List


def flip(arr: List[int], k: int):
    """k is 0 indexed"""
    i = 0
    j = k
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # result
        result = []
        lArr = len(arr)
        for i in range(lArr, 0, -1):
            # find index of i in arr
            idx = -1
            for j in range(0, i):
                if arr[j] == i:
                    idx = j
                    break
            # if index of i == i - 1 continue
            if idx == i-1:
                continue
            else:
                flip(arr, idx)
                flip(arr, i-1)
                result.append(idx+1)
                result.append(i)
        return result
