# https://leetcode.com/problems/car-fleet/

from typing import List


def canCatchUp(front, back, target):
    tf = (target-front[0]) / front[1]
    tb = (target-back[0]) / back[1]
    return tb <= tf


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        kk = []
        for i in range(len(position)):
            kk.append((position[i], speed[i]))
        kk.sort(reverse=True)
        mono = []
        fleets = 0
        for k in kk:
            # No cars after
            if len(mono) == 0:
                mono.append(k)
                continue

            if canCatchUp(mono[0], k, target):
                mono.append(k)
            else:
                fleets += 1
                mono.clear()
                mono.append(k)
        if len(mono) != 0:
            fleets += 1
        return fleets
