class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = list(map(lambda x : 60 * int(x[:2]) + int(x[3:5]), timePoints))
        mins.sort()

        ans = 1440 - mins[-1] + mins[0] 
        
        for i in range(len(mins) - 1):
            ans = min(ans, mins[i + 1] - mins[i])
        
        return ans
        
