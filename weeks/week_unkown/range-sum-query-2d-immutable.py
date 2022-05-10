class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M , N = len(matrix), len(matrix[0])
        prefix = [([0] * (N + 1)) for _ in range(M + 1)]
                
        for i in range(1, M + 1):
            row_sum = 0
            for j in range(1, N + 1):
                row_sum += matrix[i-1][j-1]
                prefix[i][j] = row_sum + prefix[i-1][j]
                
        self.prefix = prefix
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        
        a = self.prefix[row1 - 1][col1 - 1]
        b = self.prefix[row2][col1 - 1]
        c = self.prefix[row1 - 1][col2]
        d = self.prefix[row2][col2]
        
        res = d - (b + c - a)
        return res
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
