class Solution:
    def dfs(self, city, isConnected, visited):
        """Add all cities connected to city to visited"""
        visited.add(city)

        for i in range(len(isConnected)):
            if isConnected[city][i] == 1 and not i in visited:
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        for i in range(len(isConnected)):
            if i in visited:
                continue
            else:
                provinces += 1
                self.dfs(i, isConnected, visited)

        return provinces
