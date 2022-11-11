class Solution:
    def minimumBoxes(self, n: int) -> int:
        def gaussSum(x):
            return (x * (x + 1)) // 2

        latest_num = 1
        ans = num = 0

        while num + gaussSum(latest_num) < n:
            num += gaussSum(latest_num)
            ans += latest_num
            latest_num += 1

        best = left = 0
        right = latest_num

        while left <= right:
            mid = (left + right) // 2
            val = gaussSum(mid)

            if num + val >= n:
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans + best
