class Solution:
    def minimumBuckets(self, street: str) -> int:
        s = list(street)
        buckets = 0
        for i in range(1,len(s)-1):
            if s[i] == "." and s[i-1] == "H" and s[i+1] == "H":
                s[i-1] = None
                s[i+1] = None
                buckets += 1
        
        for i in range(len(s)):
            if s[i] == "." and i - 1 >= 0 and s[i-1] == "H":
                buckets += 1
                s[i-1] = None
            elif s[i] == "." and i + 1 < len(s) and s[i + 1] == "H":
                buckets += 1
                s[i +1] = None
        
        if "H" in s:
            return -1
        
        return buckets
