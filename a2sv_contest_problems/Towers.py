from heapq import heappush, heapreplace
from math import inf
from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
heap = [inf]

for n in arr:
    if heap[0] <= n:
        heappush(heap, n)
    else:
        heapreplace(heap, n)

print(len(heap) - 1)
