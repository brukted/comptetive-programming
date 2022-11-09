from collections import defaultdict, deque

n = int(input())
edges = defaultdict(set)

for _ in range(n - 1):
    x, y = map(int, input().split())
    edges[x].add(y)
    edges[y].add(x)

arr = list(map(int, input().split()))

visited = {1}
queue = deque([1])

for idx, j in enumerate(arr):
    unvisited = 0
    for nei in edges[j]:
        if nei not in visited:
            unvisited += 1    
    for nei in arr[len(visited) : len(visited) + unvisited]:
        if nei in visited or nei not in edges[j]:
            print("No")
            exit()
        else:
            visited.add(nei)

print("Yes")