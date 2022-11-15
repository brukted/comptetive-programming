class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        seen_count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # right column, lower row, left column, upper row
        bounds = [cStart + 1, rStart + 1, cStart - 1, rStart - 1]

        direction = 0
        row, col = rStart, cStart
        result = []

        seen_count = 0

        while seen_count < rows * cols:
            if 0 <= row < rows and 0 <= col < cols:
                result.append([row, col])
                seen_count += 1

            if (direction == 0 or direction == 2) and col == bounds[direction]:
                bounds[direction] += directions[direction][1]
                direction = (direction + 1) % 4

            if (direction == 1 or direction == 3) and row == bounds[direction]:
                bounds[direction] += directions[direction][0]
                direction = (direction + 1) % 4

            di, dj = directions[direction]
            row, col = row + di, col + dj

        return result
