class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIR_VECS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)

        def is_inbound(i, j): return 0 <= i < N and 0 <= j < N

        min_time_taken_grid = [[float("inf")
                                for j in range(N)] for i in range(N)]
        min_time_taken_grid[0][0] = 0
        bfsDeq = deque([(0, 0)])

        while bfsDeq:
            i, j = bfsDeq.popleft()
            if i == j and i == N - 1:
                continue
            time = min_time_taken_grid[i][j]
            for di, dj in DIR_VECS:
                ni, nj = i + di, j + dj
                if is_inbound(ni, nj) and max(grid[ni][nj], time) < min_time_taken_grid[ni][nj]:
                    min_time_taken_grid[ni][nj] = max(
                        grid[ni][nj], time, grid[i][j])
                    bfsDeq.append((ni, nj))
        return min_time_taken_grid[-1][-1]
