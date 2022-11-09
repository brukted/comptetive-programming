from collections import deque
from heapq import heapify
from sys import stdin, stdout

from numpy import array

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    arr = zip(map(int, stdin.readline().split()), range(1, n + 1))
    arr_max = list(map(lambda x: (-x[0], x[1]), arr))
    heapify(arr)
    heapify(arr_max)

    ans = []
