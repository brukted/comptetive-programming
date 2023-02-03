class Solution:
    def __init__(self, w: List[int]):
        self.prefix_array = []
        prefix = 0

        for num in w:
            prefix += num
            self.prefix_array.append(prefix)

    def pickIndex(self) -> int:
        left = 0
        right = len(self.prefix_array)
        best = 0
        rnd = random.random() * self.prefix_array[-1]

        while left <= right:
            mid = (left + right) // 2
            val = self.prefix_array[mid]

            if rnd <= val:
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return best


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
