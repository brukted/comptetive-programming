from sys import stdin, stdout
from collections import deque
from math import inf

n = int(stdin.readline().strip())
cost = list(map(int, stdin.readline().split()))
next_room = list(map(lambda x: int(x) - 1, stdin.readline().split()))

in_degree = [0 for _ in range(n)]

for nex in next_room:
    in_degree[nex] += 1

start = list(filter(lambda x: in_degree[x] == 0, range(n)))
visited = set(start)
queue = deque(start)

while queue:
    node = queue.popleft()
    nex = next_room[node]
    in_degree[nex] -= 1

    if in_degree[nex] == 0:
        queue.append(nex)
        visited.add(nex)

# print(visited)
ans = 0

for room in range(n):
    if room in visited:
        continue

    c = inf

    while room not in visited:
        visited.add(room)
        c = min(cost[room], c)
        room = next_room[room]

    # print(c, room, visited)
    ans += c

print(ans)
