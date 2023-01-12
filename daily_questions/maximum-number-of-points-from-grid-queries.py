class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_idx = [(queries[idx], idx) for idx in range(len(queries))]
        query_idx.sort(reverse=True)

        result = [None for _ in range(len(queries))]

        visited = {(0, 0)}
        seen = 0
        heap = [(grid[0][0], 0, 0)]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        while query_idx:
            val, idx = query_idx.pop()

            while heap and heap[0][0] < val:
                _, i, j = heappop(heap)
                seen += 1

                for (ni, nj) in map(lambda dir: (i + dir[0], j + dir[1]), dirs):
                    if 0 <= ni < ROWS and 0 <= nj < COLS and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        heappush(heap, (grid[ni][nj], ni, nj))

            result[idx] = seen

        return result
