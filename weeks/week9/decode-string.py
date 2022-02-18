class Solution:
    def decodeStringAsArray(self, s: str):
        result = []
        l = len(s)
        i = 0
        while i < l:
            # Numeber encountered
            if s[i].isnumeric():
                n = 0
                while s[i].isnumeric():
                    n *= 10
                    n += int(s[i])
                    i += 1
                start = i + 1
                i += 1
                opened = 1
                while opened and i < l:
                    if s[i] == '[':
                        opened += 1
                    elif s[i] == ']':
                        opened -= 1
                    i += 1
                result += n * self.decodeStringAsArray(s[start:i-1])
            else:
                result.append(s[i])
                i += 1
        return result

    def decodeString(self, s: str) -> str:
        return ''.join(self.decodeStringAsArray(s))
