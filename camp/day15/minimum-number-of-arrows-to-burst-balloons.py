class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        inter = points[0][0] , points[0][1]
        arrows = 1
        
        for point in points:
            inter = max(inter[0],point[0]) , min(inter[1] , point[1])
            
            if inter[1] >= inter[0]:
                continue
            else:
                arrows += 1
                inter = point
        return arrows