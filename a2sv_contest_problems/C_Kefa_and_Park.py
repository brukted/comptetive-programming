from collections import defaultdict, deque
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

tree = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

queue = deque([(0, arr[0], -1)])
ans = 0

while queue:
    node, cats, parent = queue.popleft()
    
    if cats > m:
        continue

    if len(tree[node]) == 1 and node != 0:
        ans += 1
        continue

    for nei in tree[node]:
        if nei == parent:
            continue
        queue.append((nei, (cats + arr[nei]) * arr[nei], node))

print(ans)
