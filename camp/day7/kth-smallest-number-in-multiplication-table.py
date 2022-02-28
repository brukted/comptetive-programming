class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        i = 1
        j = m * n
        best = None

        while i <= j:
            mid = (i + j) // 2
            nums_smaller = 0
            for row in range(1, m+1):
                nums_smaller += min(n, mid//row)
            if nums_smaller < k:
                i = mid + 1
            else:
                j = mid - 1
                best = mid
        return best
