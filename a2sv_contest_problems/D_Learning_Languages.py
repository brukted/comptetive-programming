from sys import stdin, stdout

n, m = map(int, stdin.readline().strip().split())


class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, k):
        if k not in self.parent:
            self.parent[k] = k

        if self.parent[k] == k:
            return k
        p = self.parent[k] = self.find(self.parent[k])
        return p

    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p == b_p:
            return
        self.parent[b_p] = a_p


unionFind = UnionFind()
used_langs = set()

for i in range(1, n + 1):
    langs = list(map(int, stdin.readline().strip().split()))[1:]
    for l in langs:
        used_langs.add(-l - 10)
        unionFind.union(-l - 10, i)

pp = set()

for i in range(1, n + 1):
    pp.add(unionFind.find(i))

for i in used_langs:
    pp.add(unionFind.find(i))

if len(used_langs) == 0:
    print(n)
else:
    print(len(pp) - 1)
