t = int(input())

for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = a[0] - b[0]

    for i in range(1, n):
        diff = max(diff, a[i] - b[i])

    if diff < 0:
        print("NO")
        continue

    ans = "YES"

    for i in range(n):
        if b[i] > a[i]:
            ans = "NO"
            break

        if b[i] == 0 and a[i] <= diff: # Exausted
            continue
        elif  b[i] == 0:
            ans = "NO"
            break

        if a[i] - b[i] != diff:
            ans = "NO"
            break

    print(ans)
