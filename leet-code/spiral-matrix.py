class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        M, N = len(matrix), len(matrix[0])
        
        is_inbound = lambda i, j : 0<= i < M and 0 <= j < N and matrix[i][j] is not -200
        
        i, j = 0 ,0
        ii = 0
        result = []
        
        for _ in range(N * M):
            result.append(matrix[i][j])
            matrix[i][j] = -200
            di, dj = dirs[ii]
            
            if not is_inbound(i + di, j + dj):
                ii += 1
                ii %= 4
                di, dj = dirs[ii]
            
            i, j = i + di, j + dj
    
        return result
        
        