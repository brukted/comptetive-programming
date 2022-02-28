class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        left_r = 0
        right_r = len(matrix) - 1

        # Find the row
        while left_r <= right_r:
            mid = (left_r + right_r) // 2
            start, end = matrix[mid][0], matrix[mid][-1]
            if start > target:
                right_r = mid - 1
            elif end < target:
                left_r = mid + 1
            else:
                i = mid
                break

        left = 0
        right = len(matrix[i]) - 1
        row = matrix[i]
        # Find the item
        while left <= right:
            mid = (left+right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False
