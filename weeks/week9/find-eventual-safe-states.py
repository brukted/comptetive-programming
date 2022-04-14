class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        
        @lru_cache(None)
        def isSafeNode(idx):
            if idx in visited:
                return False
            
            visited.add(idx)
            
            for i in graph[idx]:
                if not isSafeNode(i):
                    return False
            
            visited.remove(idx)
            return True
        
        safe_states = []
        for i in range(len(graph)):
            if isSafeNode(i):
                safe_states.append(i)
        return safe_states