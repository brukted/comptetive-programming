from sys import stdin, stdout


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


n, d = map(int, stdin.readline().split())

union_find = 