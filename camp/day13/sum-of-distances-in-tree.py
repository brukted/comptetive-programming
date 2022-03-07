class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case 1 : no connections
        if n == 1:
            return [0]
        
        adj_map = {}
        for a , b in edges:
            if a in adj_map:
                adj_map[a].append(b)
            else:
                adj_map[a] = [b]
            
            if b in adj_map:
                adj_map[b].append(a)
            else:
                adj_map[b] = [a]
        lower_nodes = [None for i in range(n)] 
        ans = [None for i in range(n)]
        visited = [False for i in range(n)]
        visited[0] = True
        
        def bfs(i = 0):
            distance_sum = 0
            subtree_nodes = 0
            for j in adj_map[i]:
                if visited[j]:
                    continue
                visited[j] = True
                a , b = bfs(j)
                distance_sum += a
                subtree_nodes += b
            lower_nodes[i] = distance_sum + subtree_nodes , subtree_nodes + 1
            return distance_sum + subtree_nodes , subtree_nodes + 1
        bfs()
        
        # Reset visited array
        for i in range(1,n):
            visited[i] = False
        
        def findAns(i= 0 ,parent = (0,0)):
            ans[i] = lower_nodes[i][0] + parent[0] + parent[1]    
            for j in adj_map[i]:
                if visited[j]:
                    continue  
                visited[j] = True
                nodes = parent[1] + lower_nodes[i][1] - lower_nodes[j][1]
                distance = parent[0] + parent[1] + lower_nodes[i][0] - lower_nodes[j][0] - lower_nodes[j][1] 
                findAns(j,(distance,nodes))
        
        findAns()
        return ans