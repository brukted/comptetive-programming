n = int(input())

ax, ay = map(lambda x: int(x), input().split())
bx, by = map(lambda x: int(x), input().split())
cx, cy = map(lambda x: int(x), input().split())

r = (bx < ax) == (cx < ax)
c = (by < ay) == (cy < ay)

ans = r & c 

print("YES" if ans else "NO")
