class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        bits = [0] * 10
        ans = []

        def add_to_ans():
            hour = sum(map(lambda i: 2**i * bits[i], range(4)))
            minutes = sum(map(lambda i: 2 ** (i - 4) * bits[i], range(4, 10)))
            ans.append(
                str(hour) + ":" + ("0" if minutes // 10 == 0 else "") + str(minutes)
            )

        def solve(rem=turnedOn, i=0):
            if i == 10:
                if rem == 0:
                    add_to_ans()
                return

            bits[i] = 1
            solve(rem - 1, i + 1)

            if 10 - i > rem:
                bits[i] = 0
                solve(rem, i + 1)

        solve()
        return ans
