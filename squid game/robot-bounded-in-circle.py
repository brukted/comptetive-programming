class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        curr_dir = 0
        x = y = 0

        for i in instructions:
            if i == "L":
                curr_dir = (curr_dir - 1) % 4
            elif i == "R":
                curr_dir = (curr_dir + 1) % 4
            else:
                nx, ny = x + directions[curr_dir][0], y + directions[curr_dir][1]
                x, y = nx, ny

        return x == 0 and y == 0 or curr_dir != 0
