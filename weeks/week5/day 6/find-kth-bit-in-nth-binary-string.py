# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def binaryString(self, n: int):
        if n == 1:
            return ["0"]
        n_1 = self.binaryString(n-1)
        n_1.append("1")
        l = len(n_1)
        for i in range(l-2, -1, -1):
            if n_1[i] == "0":
                n_1.append("1")
            else:
                n_1.append("0")
        return n_1

    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        if n == 1:
            return "0"
        return self.binaryString(n)[k-1]
