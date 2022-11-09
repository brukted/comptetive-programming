from string import ascii_lowercase
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
        b_p = self.find(b)
        self.parent[b_p] = a_p


t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    s = input()

    unionFind = UnionFind(ascii_lowercase)

    for ch in s:
        if k == 0:
            break
        ch = unionFind.find(ch)

        while k and ch != 'a':
            unionFind.union(chr(ord(ch) - 1), ch)
            ch = unionFind.find(ch)
            k -= 1

    out = ''.join(list(map(lambda ch: unionFind.find(ch), s)))
    stdout.write(out)
    stdout.write('\n')
