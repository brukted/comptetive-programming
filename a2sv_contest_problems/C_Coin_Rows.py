t = int(input())

for _ in range(t):
    m = int(input())
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    
    br1 = sum(r1) - r1[0]
    br2 = 0
    maxx = max(br1, br2)

    for i in range(1, m):
        br1 -= r1[i]
        br2 += r2[i-1]
        maxx = min(maxx, max(br1, br2))

    print(maxx)
