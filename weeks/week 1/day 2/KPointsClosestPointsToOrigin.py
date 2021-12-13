# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List


def greater(pointD):
    return pointD[0]


class Solution:
    def euclid_distance(self, x, y):
        return sqrt(x**2+y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointD = []
        for point in points:
            pointD.append((self.euclid_distance(point[0], point[1]), point))
        pointD.sort(key=greater)
        result = []
        for i in range(k):
            result.append(pointD[i][1])
        return result
