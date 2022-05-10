class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        count = {}
        maxx = 0
        
        while j < len(fruits):
            if fruits[j] in count:
                count[fruits[j]] += 1
                j += 1
            elif len(count) == 1:
                count[fruits[j]] = 1
                j += 1
            else:
                maxx = max(maxx, sum(count.values()))
                while len(count) == 2:
                    count[fruits[i]] -= 1
                    if count[fruits[i]] == 0:
                        count.pop(fruits[i])
                        i += 1
                        break
                    
                    i += 1
                count[fruits[j]] = 1
                j += 1
        
        maxx = max(maxx, sum(count.values()))
        return maxx
                
