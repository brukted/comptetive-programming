class Solution:
    def negativesInArow(self, row):
        left = 0
        right = len(row) - 1
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] >= 0:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        if best == -1:
            return 0
        return len(row) - best

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += self.negativesInArow(row)
        return count
