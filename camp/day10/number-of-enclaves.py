class Solution:
    def __init__(self):
        self.DIR_VECS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def markIsland(self, start_land, world):
        """Returns a boolean whether this isLand is bounded"""
        i, j = start_land
        world[i][j] = 0
        is_bounded = True

        lands = 1

        for vec in self.DIR_VECS:
            ni, nj = i + vec[0], j + vec[1]
            is_place_bounded = 0 <= ni < len(world) and 0 <= nj < len(world[0])
            is_bounded &= is_place_bounded
            if is_place_bounded and world[ni][nj] == 1:
                a, b = self.markIsland((ni, nj), world)
                is_bounded &= a
                lands += b

        return (is_bounded, lands)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        bounded_lands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                is_bounded, island_size = self.markIsland((i, j), grid)
                bounded_lands += island_size if is_bounded else 0

        return bounded_lands
