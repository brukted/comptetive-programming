class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        seen = set()
        i = 0
        j = 9
        ans = set()
        while j < len(s):
            if s[i:j+1] in seen and s[i:j+1] not in ans:
                ans.add(s[i:j+1])
            else:
                seen.add(s[i:j+1])
            i+= 1
            j += 1
        return ans
                
