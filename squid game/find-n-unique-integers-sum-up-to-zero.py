class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, n)] + [-(n * (n - 1)) // 2]
