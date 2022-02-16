class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        mdu = (10 ** 9) + 7
        return (pow(5, ceil(n / 2), mdu) * pow(4, (n // 2), mdu)) % mdu
