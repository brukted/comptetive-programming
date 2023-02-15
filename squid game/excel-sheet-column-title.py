class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = []

        while columnNumber != 0:
            curr = (columnNumber - 1) % 26
            num.append(chr(97 + curr).upper())
            columnNumber = (columnNumber - 1) // 26

        return "".join(reversed(num))
