class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        count = count.items()
        heap = []
        for key, val in count:
            heapq.heappush(heap, (-1 * val, key))
        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans
