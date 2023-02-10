class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        answer = 0

        for key, value in count.items():
            if len(key) < len(target) and target[:len(key)] == key:
                if target[len(key):] != key:
                    answer += value * count[target[len(key):]]
                else:
                    answer += (value * (value - 1))
        
        return answer
