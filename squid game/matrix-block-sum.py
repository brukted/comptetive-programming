class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])

        prefix_sum = []

        for row in mat:
            prefix = 0
            prefix_sum.append([])
            for cell in row:
                prefix += cell
                prefix_sum[-1].append(prefix)
            prefix_sum[-1].append(0)

        answer = [[0 for _ in range(N)] for _ in range(M)]

        for rIdx in range(M):
            for cIdx in range(N):
                for i in range(max(0, rIdx - k), min(M, rIdx + k + 1)):
                    answer[rIdx][cIdx] += (
                        prefix_sum[i][min(N - 1, cIdx + k)]
                        - prefix_sum[i][max(-1, cIdx - k - 1)]
                    )

        return answer
