class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = list(map(lambda x: -x, nums))
        heapify(heap)

        answer = 0
        for _ in range(k):
            answer -= heap[0]
            heapreplace(heap, -ceil((-heap[0]) / 3))

        return answer
