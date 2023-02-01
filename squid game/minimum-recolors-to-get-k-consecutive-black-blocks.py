class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = inf
        j = 0
        count = {"W": 0, "B": 0}
        for i in range(len(blocks) - k + 1):
            while j < len(blocks) and j < i + k:
                count[blocks[j]] += 1
                j += 1
            answer = min(answer, count["W"])
            count[blocks[i]] -= 1
        return answer
