class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start = None
        for i in graph.keys():
            if len(graph[i]) == 1:
                start = i
                break

        answer = [start]

        while answer[-1] == start or len(graph[answer[-1]]) != 1:
            for nei in graph[answer[-1]]:
                if len(answer) == 1 or nei != answer[-2]:
                    answer.append(nei)
                    break

        return answer
