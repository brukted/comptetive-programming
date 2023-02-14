class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = Counter(s)
        answer = count['a']
        left_count = {'a':0,'b':0}

        for ch in s:
            left_count[ch] += 1
            count[ch] -= 1
            answer = min(answer, left_count['b'] + count['a'])
        
        return answer
