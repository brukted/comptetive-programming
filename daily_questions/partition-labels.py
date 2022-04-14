class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        minMax = {}
        for idx , ch in enumerate(s):
            if not ch in minMax:
                minMax[ch] = [idx,idx]
                continue
            minMax[ch][1] = idx
        
        intervals = sorted(list(minMax.values()))
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            last = merged[-1]
            if last[1] >= intervals[i][0]:
                merged[-1] = (last[0],max(last[1],intervals[i][1]))
            else:
                merged.append(intervals[i])
        
        return [ j - i + 1 for i,j in merged]
        
