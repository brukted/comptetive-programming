class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pairs = {
            ("I", "V"): 4,
            ("I", "X"): 9,
            ("X", "L"): 40,
            ("X", "C"): 90,
            ("C", "D"): 400,
            ("C", "M"): 900,
        }
        i = 0
        ans = 0

        while i < len(s):
            if i == len(s) - 1:
                ans += values[s[i]]
                i += 1
                continue

            ch = s[i]
            next_ch = s[i + 1]

            if (ch, next_ch) in pairs:
                ans += pairs[(ch, next_ch)]
                i += 2
            else:
                ans += values[ch]
                i += 1

        return ans
