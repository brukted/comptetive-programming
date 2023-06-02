class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        groupMembers = defaultdict(list)
        groupIndegreeCount = defaultdict(int)
        indegreeCount = defaultdict(int)
        
        for idx, bIts in enumerate(beforeItems):
            if idx not in graph:
                graph[idx] = set()
            
            gg = group[idx] if group[idx] != -1 else (-1 - idx)
            groupMembers[gg].append(idx)
            
            for fr in bIts:
                if group[fr] != gg:
                    groupIndegreeCount[gg] += 1
                
                graph[fr].add(idx)
                indegreeCount[idx] += 1
        
        startingGroups = list(filter(lambda x : groupIndegreeCount[x] == 0, groupMembers.keys()))
        que = deque(startingGroups)
        ans = []
        
        while que:
            g = que.popleft()
            startingNodes = list(filter(lambda x : indegreeCount[x] == 0, groupMembers[g]))
            que2 = deque(startingNodes)
            
            while que2:
                node = que2.popleft()
                ans.append(node)
                
                for nei in graph[node]:
                    gg = (-1 - nei) if group[nei] == -1 else group[nei]
                    indegreeCount[nei] -= 1
                    
                    if gg != g:
                        groupIndegreeCount[gg] -= 1
                    
                    if indegreeCount[nei] == 0 and gg == g:
                        que2.append(nei)
                
                    if gg != g and groupIndegreeCount[gg] == 0:
                        que.append(gg)
        
        if len(ans) < n:
            return []
        
        return ans