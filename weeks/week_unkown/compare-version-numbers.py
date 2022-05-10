class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
            
        for idx, d in enumerate(v1):
            if idx >= len(v2):
                break
            if v1[idx] > v2[idx]:
                return 1
            elif v1[idx] < v2[idx]:
                return -1
        
        if len(v1) > len(v2):
            if sum(v1[len(v2):]) > 0:
                return 1
            else: 
                return 0
            
        elif len(v2) > len(v1):
            if sum(v2[len(v1):]) > 0:
                return -1
            else:
                return 0
        
        else:
            return 0
