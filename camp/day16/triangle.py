class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        HEIGHT = len(triangle)

        is_inbound = lambda row , i : 0 <= i < len(triangle[row])        
        memo = defaultdict(int)
        
        def minPathSumRec(row = 0 ,i = 0):
            if row == HEIGHT - 1:
                memo[(row,i)] = triangle[row][i]
            else:
                down = float("inf")
                down_right = float("inf")
                if is_inbound(row+1,i):
                    down = memo[(row+1,i)] if (row+1,i) in memo else minPathSumRec(row + 1,i)
                if is_inbound(row+1,i+1):
                    down_right = memo[(row+1,i+1)] if (row+1,i+1) in memo else minPathSumRec(row + 1, i + 1)
                
                memo[(row,i)] = min(down,down_right) + triangle[row][i]
            
            return memo[(row,i)]
                
        minPathSumRec()
        return memo[(0,0)]
        