class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        a = 0
        count = 0
        l = len(chars)
        result = []
        while j < l:
            while j < l and chars[i] == chars[j]:
                count += 1
                j += 1
            chars[a] = chars[i]
            a += 1
            if count > 1:
                digC = str(count)
                for c in digC:
                    chars[a] = c
                    a += 1
            count = 0
            i = j
        return a

