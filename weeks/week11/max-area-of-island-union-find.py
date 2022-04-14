class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        DIRS = [(-1,0),(1,0),(0,1),(0,-1)]
        
        is_inbound = lambda i,j : 0  <= i < M and 0 <= j < N
        parents = {}
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    parents[(i,j)] = (i,j)
        
        def findParent(i):
            if parents[i] == i:
                return i
            p = findParent(parents[i])
            parents[i] = p
            return p
        
        def connect(place1,place2):
            root_1 = findParent(place1)
            root_2 = findParent(place2)
            if root_1 != root_2:
                parents[root_1] = root_2
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    for di, dj in DIRS:
                        if is_inbound(di + i,dj + j) and grid[di + i][dj + j] == 1:
                            connect((di+i,dj+j),(i,j))
        
        for place in parents.keys():
            findParent(place)
        
        sizes = Counter(parents.values()).values()
        
        return 0 if not sizes else max(sizes)
