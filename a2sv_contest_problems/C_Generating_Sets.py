import heapq


_ = int(input())
y = list(map(int, input().split()))

used = set(y)
h = list(map(lambda x: -x, y))
heapq.heapify(h)
ans = []
while h:
    num = -heapq.heappop(h)
    
    b = num
    while b > 0 and b in used:
        b //= 2

    if b == 0:
        ans.append(num)
    else:
        used.add(b)
        heapq.heappush(h, -b)

print(*ans)
