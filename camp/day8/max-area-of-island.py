class Solution:
    """ Coords is like matrix in math"""

    def __init__(self):
        self.DIR_VECS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def isInBound(self, world, coord):
        return len(world) > coord[0] >= 0 and len(world[0]) > coord[1] >= 0

    def islandSize(self, world, place):
        assert world[place[0]][place[1]] != 0

        size = 1
        world[place[0]][place[1]] = 0

        for dirVec in self.DIR_VECS:
            new_place = place[0] + dirVec[0], place[1] + dirVec[1]
            if self.isInBound(world, new_place) and world[new_place[0]][new_place[1]] == 1:
                size += self.islandSize(world, new_place)

        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.islandSize(grid, (i, j)))

        return max_area
