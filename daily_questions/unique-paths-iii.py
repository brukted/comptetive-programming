class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        VECS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        is_inbound = lambda i, j: 0 <= i < M and 0 <= j < N
        starting = (-1, -1)
        ending = (-2, -2)
        non_obstacles = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    non_obstacles += 1
                elif grid[i][j] == -1:
                    continue
                elif grid[i][j] == 1:
                    starting = (i, j)
                elif grid[i][j] == 2:
                    ending = (i, j)

        walked = set()

        def dfs_unique_paths(place=starting):
            if place == ending:
                return 1 if len(walked) - 1 == non_obstacles else 0
            walked.add(place)
            unique_paths = 0
            for di, dj in VECS:
                ni, nj = place[0] + di, place[1] + dj
                if is_inbound(ni, nj) and (ni, nj) not in walked and grid[ni][nj] != -1:
                    unique_paths += dfs_unique_paths((ni, nj))
            walked.remove(place)
            return unique_paths

        return dfs_unique_paths()
