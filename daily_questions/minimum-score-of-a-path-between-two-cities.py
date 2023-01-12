class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for (a, b, d) in roads:
            graph[a - 1].append((b - 1, d))
            graph[b - 1].append((a - 1, d))

        visited = [False for _ in range(n)]
        visited[0] = True
        queue = deque([0])
        answer = inf

        while queue:
            node = queue.popleft()

            for (a, d) in graph[node]:
                answer = min(answer, d)
                if not visited[a]:
                    queue.append(a)
                visited[a] = True

            graph[node] = []

        return answer
