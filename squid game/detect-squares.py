class DetectSquares:
    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_count[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        answer = 0

        for x1, y1 in list(self.point_count.keys()):
            if abs((x1 - x) * (y1 - y)) < 0.0001 or abs(x1 - x) != abs(y1 - y):
                continue
            answer += (
                self.point_count[(x1, y1)]
                * self.point_count[(x1, y)]
                * self.point_count[(x, y1)]
            )

        return answer


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
