class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()
        
        if len(s) != len(t):
            return False
        
        for idx, letter in enumerate(s):
            if letter not in mapping:
                
                if t[idx] in mapped:
                    return False
                
                mapping[letter] = t[idx]
                mapped.add(t[idx])
            
            elif mapping[letter] != t[idx]:
                return False
        
        return True
