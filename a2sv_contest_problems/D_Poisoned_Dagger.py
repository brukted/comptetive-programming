import heapq


t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))

    duration_heap = []

    for i in range(n - 1):
        duration_heap.append(arr[i+1] - arr[i])
    
    duration_heap.sort()

    damage = 0
    k = 0
    i = 0
    while damage < h and i < n:
        damage += 


