class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        a = a[::-1]
        b = b[::-1]

        result = []
        carry = 0
        for i in range(min(len(a), len(b))):
            carry += int(a[i]) + int(b[i])
            result.append(str(carry % 2))
            carry //= 2

        for i in range(len(b), len(a)):
            carry += int(a[i])
            result.append(str(carry % 2))
            carry //= 2

        while carry != 0:
            result.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(result))
