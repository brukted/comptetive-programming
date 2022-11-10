class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1

        for index, (x1, y1) in enumerate(points):
            for index_2 in range(index + 1, len(points)):
                x2, y2 = points[index_2]

                if x1 == x2:
                    curr = 2
                    for index_3 in range(index_2 + 1, len(points)):
                        if points[index_3][0] == x1:
                            curr += 1
                    ans = max(ans, curr)
                    continue

                m = (y1 - y2) / (x1 - x2)
                b = y1 - (m * x1)

                curr = 2
                for index_3 in range(index_2 + 1, len(points)):
                    x, y = points[index_3]
                    if abs((x * m) + b - y) < 0.00001:
                        curr += 1

                ans = max(curr, ans)

        return ans
