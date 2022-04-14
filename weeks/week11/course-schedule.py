class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_count = [0 for _ in range(numCourses)]
        adj_map = defaultdict(list)
        for cour, pre in prerequisites:
            adj_map[pre].append(cour)
            dep_count[cour] += 1
        
        queue = deque(filter(lambda x: dep_count[x] == 0,range(numCourses)))
        visited = 0
        
        while queue:
            course = queue.popleft()
            visited += 1
            for sub_course in adj_map[course]:
                dep_count[sub_course] -= 1
                if dep_count[sub_course] == 0:
                    queue.append(sub_course)
        
        return visited == numCourses
