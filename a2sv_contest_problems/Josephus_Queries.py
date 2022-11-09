from os import remove
from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    removed = 0

    while removed + n // 2 < k:
        removed += n // 2

    if removed == n - 1:
        print(1)
    else:
        print(((k - removed) * d))
