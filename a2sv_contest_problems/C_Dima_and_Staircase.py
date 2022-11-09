n = int(input())
a = list(map(int, input().split()))
m = int(input())

height = a[0]
width = 1

for _ in range(m):
    w, h = map(int, input().split())

    if width == n:
        print(height)
        height += h

    else:
        height = max(height, a[w - 1])
        print(height)
        height += h

        while width <= n and a[width - 1] < height:
            width += 1
        