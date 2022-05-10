class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        def search(start, target):
            end = len(events) - 1
            ans = -1
            
            while (start <= end):
                mid = (start + end) // 2
                
                if (events[mid][0] <= target):
                    start = mid + 1
                else:
                    ans = mid
                    end = mid - 1

            return ans
        
        
        next_best_event = [None] * len(events)
        next_best_event[-1] = events[-1][2]
        
        for i in range(len(events) - 2, -1, -1):
            next_best_event[i] = max(next_best_event[i + 1] , events[i][2])
           
        maxx = 0
        
        for idx , (s, e, val) in enumerate(events):
            j = search(idx + 1, e)
            if j != -1:
                curr = val + next_best_event[j]
                maxx = max(maxx, curr)
            else:
                maxx = max(maxx, val)
        
        return maxx
