class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)

        for (a, b) in edges:
            graph[a].append(b)
            graph[b].append(a)

        for node in range(len(vals)):
            graph[node].sort(key=vals.__getitem__, reverse=True)

        answer = -inf
        for node in range(len(vals)):
            curr = vals[node]
            answer = max(curr, answer)

            for i in range(min(k, len(graph[node]))):
                curr += vals[graph[node][i]]
                answer = max(curr, answer)

        return answer
