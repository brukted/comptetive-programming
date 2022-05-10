class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(strs[0])
        
        for i in range(1, len(strs)):
            s = strs[i]
            
            while len(l) > len(s):
                l.pop()
            
            for j in range(len(s)):
                if j >= len(l):
                    break
                elif l[j] != s[j]:
                    while len(l) != j:
                        l.pop()
                    break
        
        return "".join(l)
