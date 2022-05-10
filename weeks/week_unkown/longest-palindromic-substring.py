class Solution:
    def longestPalindrome(self, s: str) -> str:
        li, lj = 0, 0
        l_len = 1
        
        for idx in range(len(s)):
            i , j = idx, idx
            while i >= 0 and j < len(s) and s[i] == s[j]:
                size = j - i + 1
                if size > l_len:
                    l_len = size
                    li, lj = i, j
                i -= 1
                j += 1
            
            i, j = idx, idx + 1
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                size = j - i + 1
                if size > l_len:
                    l_len = size
                    li, lj = i, j
                i -= 1
                j += 1
        
        return s[li: lj+1]
            
        
