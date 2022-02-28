class MedianFinder:

    def __init__(self):
        self.left_half = []  # Max heap
        self.right_half = []  # Min heap

    def addNum(self, num: int) -> None:
        rh = self.right_half
        lh = self.left_half

        right_min = rh[0] if rh else float("inf")

        if num <= right_min:
            heapq.heappush(lh, -num)
        else:
            heapq.heappush(rh, num)

        if (len(lh) + len(rh)) % 2 == 0:  # Even
            if len(lh) > len(rh):
                a = -heapq.heappop(lh)
                heapq.heappush(rh, a)
            elif len(rh) > len(lh):
                a = -heapq.heappop(rh)
                heapq.heappush(lh, a)
        else:
            if len(rh) > len(lh):
                a = -heapq.heappop(rh)
                heapq.heappush(lh, a)

    def findMedian(self) -> float:
        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            return (-self.left_half[0]+self.right_half[0]) / 2
        else:
            return -self.left_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
