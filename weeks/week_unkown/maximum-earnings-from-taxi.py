class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        
        def search(start,target):
            end = len(rides) - 1

            ans = -1
            while (start <= end):
                mid = (start + end) // 2

                if (rides[mid][0] < target):
                    start = mid + 1
                else:
                    ans = mid
                    end = mid - 1

            return ans
    
        @lru_cache(None)
        def what(i):
            if i == len(rides) - 1:
                return rides[i][1] - rides[i][0] + rides[i][2]
            
            dont = what(i + 1)
            
            j = search(i + 1, rides[i][1])
            
            if j == -1: # There is no next ride
                return max(dont, rides[i][1] - rides[i][0] + rides[i][2])
            
            return max(dont, what(j) + rides[i][1] - rides[i][0] + rides[i][2])
            
        return what(0)
