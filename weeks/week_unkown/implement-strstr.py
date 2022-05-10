class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            found = True
            
            for j in range(len(needle)):
                if i + j < len(haystack) and haystack[i+j] == needle[j]:
                    continue
                else:
                    found = False
                    break
            
            if found:
                return i
        
        return -1
