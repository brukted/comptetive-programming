from collections import defaultdict

n, m = map(int, input().split())
c = list(map(int, input().split()))


class UnionFind:
    def __init__(self, items) -> None:
        self.parent = {item: item for item in items}
        self.size = {item: 1 for item in items}

    def find(self, k):
        if self.parent[k] == k:
            return k
        p = self.parent[k] = self.find(self.parent[k])
        return p

    def union(self, a, b):
        a_p = self.find(a)
        a_s = self.size[a_p]

        b_p = self.find(b)
        b_s = self.size[b_p]

        if a_p == b_p:
            return

        if a_s < b_s:
            b_p, b_s, a_p, a_s = a_p, a_s, b_p, b_s

        self.parent[b_p] = a_p
        self.size[a_p] += b_s


dsu = UnionFind(range(n))

for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    dsu.union(x, y)

group_min = defaultdict(lambda: float("inf"))

for i in range(n):
    if group_min[dsu.find(i)] > c[i]:
        group_min[dsu.find(i)] = c[i]

print(sum(list(group_min.values())))
