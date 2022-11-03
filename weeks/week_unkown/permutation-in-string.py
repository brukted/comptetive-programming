class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = s2, s1
        
        target = Counter(s2)
        def match() : return all(map(lambda x : 0 == target[x], string.ascii_lowercase))
        
        i, j = 0, 0
        
        while j < len(s1):
            if j < len(s2):
                target[s1[j]] -= 1
                j += 1
                continue
            
            if match(): return True
            target[s1[i]] += 1
            target[s1[j]] -= 1
            i, j = i + 1, j + 1
        
        return match()
                
