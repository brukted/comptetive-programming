class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dirs = [(1,0),(0,1)]
        M = len(grid)
        N = len(grid[0])
        
        if M + N == 2:
            return grid[-1][-1]
        
        is_inbound = lambda i, j : i < M and j < N
        memo = {(M - 1,N - 1) : grid[-1][-1]}
        
        def minPathSumRec(i = 0,j = 0):
            minPath = float("inf")
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if is_inbound(ni,nj):
                    if (ni, nj) not in memo:
                        minPathSumRec(ni,nj)
                    minPath = min(minPath, memo[(ni,nj)]  + grid[i][j])
            memo[(i,j)] = minPath
            
        minPathSumRec()
        return memo[(0,0)]