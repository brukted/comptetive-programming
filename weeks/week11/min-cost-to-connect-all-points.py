class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mesh_conn = []
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(mesh_conn,(distance,i,j))
        
        parents = [i for i in range(len(points))]
        
        def findParent(p):
            if parents[p] == p:
                return p
            a = findParent(parents[p])
            parents[p] = a
            return a
        
        cost_sum = 0
        while mesh_conn:
            dist, p1, p2 = heapq.heappop(mesh_conn)
            pr1 = findParent(p1)
            pr2 = findParent(p2)
            if pr1 == pr2:
                continue
            #connect(p1,p2)
            parents[pr1] = pr2
            cost_sum += dist
        
        return cost_sum
