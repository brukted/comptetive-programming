from collections import defaultdict
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())


class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.count = 0

for _ in range(n):
    word = input()
    
