t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    op = 0
    
    for n in arr[:k]:
        if n > k:
            op += 1
    
    print(op)