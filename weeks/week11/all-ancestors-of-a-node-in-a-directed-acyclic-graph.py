class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_map = defaultdict(list)

        deps_count = [0 for _ in range(n)]
        
        for start_node, end_node in edges:
            adj_map[start_node].append(end_node)
            deps_count[end_node] += 1

        ancestors_set = [set() for _ in range(n)]
                        
        queue = deque(filter(lambda i : deps_count[i] == 0, range(n)))
        
        while queue:
            node = queue.popleft()
            
            for adj_node in adj_map[node]:
                ancestors_set[adj_node] = ancestors_set[adj_node].union(ancestors_set[node])
                ancestors_set[adj_node].add(node)
                
                deps_count[adj_node] -= 1
                if deps_count[adj_node] == 0:
                    queue.append(adj_node)
                
        ancestors = []
        
        for lineage in ancestors_set:
            l = list(lineage)
            l.sort()
            ancestors.append(l)
        
        return ancestors
        
