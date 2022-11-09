n = int(input())
a = list(map(int, input().split()))

l = 1
m = 1

for i in range(1, n):
    if a[i] > a[i-1]:
        l += 1
    else:
        m = max (l ,m)
        l = 1

m = max(l, m)

print(m)