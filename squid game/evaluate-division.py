class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)

        for idx, (a, b) in enumerate(equations):
            a = "".join(sorted(a))
            b = "".join(sorted(b))
            graph[a].append((values[idx], b))
            graph[b].append((1 / values[idx], a))

        visited = set()

        def search(node, target):
            if node == target:
                return 1.0

            for val, nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    res = search(nei, target)
                    visited.remove(nei)
                    if res is not None:
                        return res * val

            return None

        res = []

        for a, b in queries:
            a, b = "".join(sorted(a)), "".join(sorted(b))
            visited.add(a)
            result = search(a, b) if a in graph and b in graph else None
            visited.remove(a)
            res.append(result if result is not None else -1)

        return res
