t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    while i < n and arr[i] == 0:
        i += 1

    if i == n or i == n - 1:
        print('0')
        continue

    # make smooth
    prefix = 0
    ops = 0
    while i < n - 1:
        if arr[i] == 0:
            ops += 1
        prefix += arr[i]
        i += 1
    print(ops + prefix)
