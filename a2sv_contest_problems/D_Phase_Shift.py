from string import ascii_lowercase
from sys import stdin, stdout

t = int(stdin.readline().strip())


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


for _ in range(t):
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()

    dsu = UnionFind(ascii_lowercase)
    nex = {}
    prev = {}
    conns = 0

    for ch in s:
        if ch in nex:
            continue

        for char in ascii_lowercase:
            if ch == char or char in prev:
                continue

            if dsu.find(char) != dsu.find(ch) or conns == 25:
                nex[ch] = char
                prev[char] = ch
                dsu.union(ch, char)
                conns += 1
                break

    print("".join(list(map(lambda x: nex[x], s))))
