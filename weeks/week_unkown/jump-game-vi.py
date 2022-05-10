class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(-nums[-1],len(nums) - 1)]
        
        for i in range(len(nums) - 2, -1, -1):
            # Remove unreachables
            while heap[0][1] > i + k:
                heapq.heappop(heap)

            best , _ = heap[0]
            best *= -1
                        
            turn = best + nums[i]
            heapq.heappush(heap, (-turn, i))
                    
        while heap:
            val, i = heapq.heappop(heap)
            if i == 0:
                return -val
