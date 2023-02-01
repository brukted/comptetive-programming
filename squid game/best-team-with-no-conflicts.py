class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        zipped = sorted(zip(ages, scores))
        best = [0 for _ in range(len(scores))]

        for i in range(len(scores)):
            age, score = zipped[i]
            for j in range(i):
                if zipped[j][1] <= score or zipped[j][0] == age:
                    best[i] = max(best[i], best[j])
            best[i] += score

        return max(best)
