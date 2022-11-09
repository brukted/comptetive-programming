n, h = map(int, input().split())
a = map(int, input().split())

min_w = 0

for i in a:
    if i <= h:
        min_w += 1
    else:
        min_w += 2

print(min_w)
