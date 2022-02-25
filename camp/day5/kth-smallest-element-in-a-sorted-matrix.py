class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix_heap = []  # (row head,row index , row item idx)
        n = len(matrix)

        # Add row heap
        for idx, row in enumerate(matrix):
            heapq.heappush(matrix_heap, (row[0], idx, 0))

        kth = None

        while k > 0:
            k -= 1
            row_head, row_idx, row_pointer = heapq.heappop(matrix_heap)
            kth = row_head
            row_pointer += 1
            # Row has ended
            if not row_pointer < n:
                continue
            row = matrix[row_idx]
            heapq.heappush(
                matrix_heap, (row[row_pointer], row_idx, row_pointer))

        return kth
