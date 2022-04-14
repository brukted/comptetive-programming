class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_map = {i : [] for i in range(numCourses)}
        
        for pre, cor in prerequisites:
            adj_map[cor].append(pre)
                
        @lru_cache(None)
        def Prerequisites(course):
            pres = set()
            for pre in adj_map[course]:
                pres = pres.union(Prerequisites(pre))
                pres.add(pre)
            return pres
        
        def processQuery(query):
            u, v = query
            if u in Prerequisites(v):
                return True
            else:
                return False
        
        ans = []
        for query in queries:
            ans.append(processQuery(query))
        return ans
