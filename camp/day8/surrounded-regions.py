class Solution:
    def __init__(self):
        self.DIR_VECS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def isInBound(self, grid, coord):
        return len(grid) > coord[0] >= 0 and len(grid[0]) > coord[1] >= 0

    def tryToCapture(self, start, board, island):
        """Adds every o to the island"""

        island.add(start)

        spill = False

        for dirVec in self.DIR_VECS:
            new_start = start[0] + dirVec[0], start[1] + dirVec[1]
            is_in_bound = self.isInBound(board, new_start)

            if not is_in_bound:  # This square spills into oblivion
                spill = True
                continue

            if is_in_bound and board[new_start[0]][new_start[1]] == 'O' and new_start not in island:
                spill |= self.tryToCapture(new_start, board, island)

        return spill

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        captured = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    continue
                elif (i, j) not in visited:
                    island = set()
                    spill = self.tryToCapture((i, j), board, island)
                    if not spill:
                        captured = set.union(island, captured)
                    visited = set.union(visited, island)

        for i, j in captured:
            board[i][j] = 'X'
