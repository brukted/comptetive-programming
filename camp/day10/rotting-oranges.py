class Solution:
    def __init__(self):
        self.DIR_VECS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def closestRottenOrange(self, start, grid, rot_time_grid, m, n):
        def is_valid(i, j): return 0 <= i < m and 0 <= j < n and (
            i, j) not in visited and grid[i][j] != 0
        bfsDeq = deque([(start, 0)])  # coord , depth
        visited = {start}
        while bfsDeq:
            pos, depth = bfsDeq.popleft()
            i, j = pos
            visited.add((i, j))
            if grid[i][j] == 2:  # Rotten orange found
                rot_time_grid[start[0]][start[1]] = min(
                    rot_time_grid[start[0]][start[1]], depth)
                break
            for vec in self.DIR_VECS:
                ni, nj = i + vec[0], j + vec[1]
                if is_valid(ni, nj):
                    bfsDeq.append(((ni, nj), depth+1))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initilize a rot grid with infinity cells
        rot_time_grid = [[float("inf") for i in range(n)] for j in range(m)]

        # Find the closest rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.closestRottenOrange((i, j), grid, rot_time_grid, m, n)

        min_rot_time = 0

        # Find the orange that takes the maximum time to rot
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_rot_time = max(rot_time_grid[i][j], min_rot_time)

        # Return -1 if there is an orange that won't rot, i.e takes inf to rot
        return min_rot_time if min_rot_time != float("inf") else -1
