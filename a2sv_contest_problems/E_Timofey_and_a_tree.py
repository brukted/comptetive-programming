from collections import defaultdict
from functools import lru_cache
n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

colors = list(map(int, input().split()))

@lru_cache(None)
def canBeRoot(root, parent=-1):
    if len(tree[root]) == 0:
        return True

    for child in tree[root]:
        if child != parent:
            same_color = colors[child] == colors[root] or parent == -1
            
            if same_color and canBeRoot(child, root):
                continue
            else:
                return False

    return True


for i in range(n):
    if canBeRoot(i):
        print("YES")
        print(i + 1)
        exit()

print("NO")
