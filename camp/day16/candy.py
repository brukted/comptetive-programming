class Solution:
    def candy(self, ratings: List[int]) -> int:
        rai = [(val,idx) for idx , val in enumerate(ratings)]
        rai.sort()
        candies = [1 for i in range(len(ratings))]
        
        for _, idx in rai:
            candy = 1
            if (idx - 1 >= 0 and ratings[idx-1] < ratings[idx]):
                candy = max(candy, candies[idx-1] + 1)
            if (idx + 1 < len(ratings) and ratings[idx+1] < ratings[idx]):
                candy = max(candy,candies[idx+1] + 1)
            candies[idx] = candy
        
        return sum(candies)