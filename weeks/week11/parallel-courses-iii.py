class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_map = defaultdict(set)
        dep_count = [0 for _ in range(n)]
        preq = [0 for _ in range(n)]
        
        for prev, cour in relations:
            adj_map[prev-1].add(cour-1)
            dep_count[cour-1] +=  1
        
        queue = deque(list(filter(lambda i: dep_count[i] == 0, range(n))))
        
        min_time = float("-inf")
        
        while queue:
            course = queue.popleft()
                        
            for child in adj_map[course]:
                preq[child] = max(preq[child], preq[course] + time[course])
                dep_count[child] -= 1
                if dep_count[child] == 0:
                    queue.append(child)
            
            if not adj_map[course]:
                min_time = max(min_time, preq[course] + time[course])
            
        return min_time
        
