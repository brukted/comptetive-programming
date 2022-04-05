class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]
        
        nia = [0 for i in range(len(security))]
        nia[0] = 1
        
        for i in range(1,len(security)):
            if security[i - 1] >= security[i]:
                nia[i] = nia[i-1] + 1
            else:
                nia[i] = 1
        
        days = []
        nda = 1
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                nda += 1
            else:
                nda = 1
            if nda > time and nia[i] > time and time <= i < len(security) - time:
                days.append(i)
                
        return days
        
