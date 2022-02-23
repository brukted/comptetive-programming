class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = count.items()
        heap = []
        for key, val in count:
            heapq.heappush(heap, (-1 * val, key))
        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans
