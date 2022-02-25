class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        best = -1

        while left <= right:
            mid = (left + right) // 2
            # mid paper has less cites than its pos, advance left
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        if best == -1:
            return 0

        return len(citations) - best
