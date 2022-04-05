class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i = 0
        j = 0
        ch_set = set()
        
        while j < len(s):
            while j < len(s) and s[j] not in ch_set:
                ch_set.add(s[j])
                j += 1
            max_length = max(max_length, j - i)
            if j < len(s):
                while s[j] in ch_set:
                    ch_set.remove(s[i])
                    i += 1
        
        return max_length
