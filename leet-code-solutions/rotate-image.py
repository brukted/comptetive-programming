class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        
        # Reverse each row
        for row in matrix:
            for i in range(len(row) // 2):
                row[i], row[~i] = row[~i], row[i]
        
        # Reverse each diagonal
        for i in range(1, N * 2):
            if i >= N:
                ui, uj = 0, i % N
                li, lj = N - 1 - i % N, N - 1
            else:
                ui, uj = N - i, 0
                li, lj = N - 1, i - 1
            
            while uj < lj:
                matrix[ui][uj], matrix[li][lj] = matrix[li][lj], matrix[ui][uj]
                ui += 1
                uj += 1
                li -= 1
                lj -= 1