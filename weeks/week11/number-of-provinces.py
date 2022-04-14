class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        sizes = [1] * len(isConnected)
        
        def findParent(i):
            if parents[i] == i:
                return i
            p = findParent(parents[i])
            parents[i] = p
            return p
        
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    root_i = findParent(i)
                    root_j = findParent(j)

                    if (sizes[root_i] < sizes[root_j]):
                        parents[root_i] = root_j
                        sizes[root_j] += sizes[root_i]
                    else:
                        parents[root_j] = root_i
                        sizes[root_i] += sizes[root_j]
        
        for i in range(len(isConnected)):
            findParent(i)
        
        return len(set(parents))
